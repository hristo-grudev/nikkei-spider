BOT_NAME = 'nikkei'

SPIDER_MODULES = ['nikkei.spiders']
NEWSPIDER_MODULE = 'nikkei.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'INFO'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'nikkei.pipelines.NikkeiPipeline': 100,

}

