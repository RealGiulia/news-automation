from searcher import Searcher
from logger import Logger
from excel import Excel
from user_input import INPUT_READER




if __name__ == "__main__":

    #setup of environment
    config = INPUT_READER()
    log_path = config.parser("LOG_FOLDER")
    excel_path = config.parser("EXCEL_FOLDER")
    img_path = config.parser("IMAGE_FOLDER")
    search_phrase = config.parser("SEARCH")
    topic = config.parser("TOPIC")
    period = config.parser("PERIOD")
    log = Logger(log_path)
    search = Searcher(img_path, log)
    excel_handler = Excel(excel_path,log)

    search.open_website()
    search.search_news(search_phrase)
    search.select_topic(topic)
    search.select_period(period)
    storage = []
    news_collected = search.get_news_info(storage)
    search.driver.close()
    search.complete_news_info(news_collected, search_phrase)
    excel_handler.insert_data(news_collected)

    print("FINALIZADO")