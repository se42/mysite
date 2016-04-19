from mezzanine.conf import register_setting

register_setting(
    name="BLOG_POST_PER_PAGE",
    label="Blog posts per page",
    description="The number of blog posts to show per page.",
    editable=True,
    default=50,
)

