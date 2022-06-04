BOT_NAME = "hots"

SPIDER_MODULES = ["hots.spiders"]
NEWSPIDER_MODULE = "hots.spiders"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    "hots.pipelines.HotsPipeline": 300,
}
