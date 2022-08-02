from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(
    feeder_threads=1,
    parser_threads=1,
    downloader_threads=1,
    storage={'root_dir': '/M/Math_memes'})
google_crawler.crawl(keyword='math meme about sum', max_num=3, file_idx_offset=0)

