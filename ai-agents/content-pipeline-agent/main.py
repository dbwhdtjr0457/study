from crewai.flow.flow import Flow, listen, start, router, and_, or_
from crewai.agent import Agent
from crewai import LLM
from pydantic import BaseModel
from tools import web_search_tool
from seo_crew import SeoCrew


class BlogPost(BaseModel):
    title: str
    subtitle: str
    sections: list[str]


class Tweet(BaseModel):
    content: str
    hashtags: str


class LinkedInPost(BaseModel):
    hook: str
    content: str
    call_to_action: str


class Score(BaseModel):
    score: int = 0
    reason: str = ""


class ContentPipelineState(BaseModel):
    # inputs
    content_type: str = ""
    topic: str = ""

    # internal
    max_length: int = 0
    score: Score | None = None
    research: str = ""

    # content
    blog_post: BlogPost | None = None
    tweet: Tweet | None = None
    linkedin_post: LinkedInPost | None = None


class ContentPipelineFlow(Flow[ContentPipelineState]):
    @start()
    def init_content_pipeline(self):
        if self.state.content_type not in ["tweet", "blog_post", "linkedin"]:
            raise ValueError("Unsupported content type")

        if self.state.topic == "":
            raise ValueError("Topic cannot be empty")

        if self.state.content_type == "tweet":
            self.state.max_length = 150
        elif self.state.content_type == "blog_post":
            self.state.max_length = 800
        elif self.state.content_type == "linkedin":
            self.state.max_length = 500

    @listen(init_content_pipeline)
    def conduct_research(self):
        researcher = Agent(
            role="Head Researcher",
            backstory="You're like a digital detective who loves digging up fascinating facts and insights. You have a knack for finding the good stuff that others miss.",
            goal=f"Find the most interesting and useful info about {self.state.topic}",
            tools=[web_search_tool],
        )

        self.state.research = researcher.kickoff(
            messages=f"Find the most interesting and useful info about {self.state.topic}"
        )

    @router(conduct_research)
    def conduct_research_router(self):
        content_type = self.state.content_type
        if content_type == "tweet":
            return "make_tweet"
        elif content_type == "blog_post":
            return "make_blog"
        elif content_type == "linkedin":
            return "make_linkedin"

    @listen(or_("make_blog", "remake_blog"))
    def handle_make_blog(self):
        blog_post = self.state.blog_post

        llm = LLM(model="openai/gpt-4o-mini", response_format=BlogPost)

        if blog_post is None:
            self.state.blog_post = llm.call(
                f"""
            Make a blog post with good SEO practices on the topic {self.state.topic} using the following research:

            <research>
            ================
            {self.state.research}
            ================
            </research>
            """
            )
        else:
            self.state.blog_post = llm.call(
                f"""
            You wrote this blog post on {self.state.topic}, but it does not have a good SEO score because of {self.state.score.reason} 
            
            Improve it.

            <blog post>
            {self.state.blog_post.model_dump_json()}
            </blog post>

            Use the following research.

            <research>
            ================
            {self.state.research}
            ================
            </research>
            """
            )

    @listen(or_("make_tweet", "remake_tweet"))
    def handle_make_tweet(self):
        Tweet = self.state.tweet

        llm = LLM(model="openai/gpt-4o-mini", response_format=Tweet)

        if Tweet is None:
            self.state.tweet = llm.call(
                f"""
            Make a tweet that can go viral on the topic {self.state.topic} using the following research:

            <research>
            ================
            {self.state.research}
            ================
            </research>
            """
            )
        else:
            self.state.tweet = llm.call(
                f"""
            You wrote this tweet on {self.state.topic}, but it does not have a good virality score because of {self.state.score.reason} 
            
            Improve it.

            <tweet>
            {self.state.tweet.model_dump_json()}
            </tweet post>

            Use the following research.

            <research>
            ================
            {self.state.research}
            ================
            </research>
            """
            )

    @listen(or_("make_linkedin", "remake_linkedin"))
    def handle_make_linkedin(self):
        LinkedInPost = self.state.linkedin_post

        llm = LLM(model="openai/gpt-4o-mini", response_format=LinkedInPost)

        if LinkedInPost is None:
            self.state.linkedin_post = llm.call(
                f"""
            Make a LinkedIn post that can go viral on the topic {self.state.topic} using the following research:

            <research>
            ================
            {self.state.research}
            ================
            </research>
            """
            )
        else:
            self.state.linkedin_post = llm.call(
                f"""
            You wrote this LinkedIn post on {self.state.topic}, but it does not have a good virality score because of {self.state.score.reason} 
            
            Improve it.

            <linkedin post>
            {self.state.linkedin_post.model_dump_json()}
            </linkedin post>

            Use the following research.

            <research>
            ================
            {self.state.research}
            ================
            </research>
            """
            )

    @listen(handle_make_blog)
    def check_seo(self):
        result = (
            SeoCrew()
            .crew()
            .kickoff(
                inputs={
                    "topic": self.state.topic,
                    "blog_post": self.state.blog_post.model_dump_json(),
                }
            )
        )

        self.state.score = result.pydantic

    @listen(or_(handle_make_tweet, handle_make_linkedin))
    def check_virality(self):
        print(self.state.tweet)
        print(self.state.linkedin_post)
        print("Checking virality potential for the post")

    @router(or_(check_seo, check_virality))
    def score_router(self):
        content_type = self.state.content_type
        score = self.state.score
        print("Score router:", score)

        if score is not None and score.score >= 8:
            return "check_passed"
        else:
            if content_type == "blog_post":
                return "remake_blog"
            elif content_type == "linkedin":
                return "remake_linkedin"
            elif content_type == "tweet":
                return "remake_tweet"

    @listen("check_passed")
    def finalize_content(self):
        print("Finalizing the content for publishing")


flow = ContentPipelineFlow()

flow.kickoff(
    inputs={
        "content_type": "blog_post",
        "topic": "artificial intelligence",
    }
)
