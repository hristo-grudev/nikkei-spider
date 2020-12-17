BOT_NAME = 'nikkei'

SPIDER_MODULES = ['nikkei.spiders']
NEWSPIDER_MODULE = 'nikkei.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'INFO'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

FEEDS = {
	'./files/items.jl': {
		'format': 'jsonlines',
		'encoding': 'utf8',
		'store_empty': False,
		'item_export_kwargs': {
			'export_empty_fields': True,
		},
	},
}

ITEM_PIPELINES = {
	# 'nikkei.pipelines.NikkeiPipeline': 100,

}

