from Setting import DefineManager
from Utils import LogManager

class CrawlBasicInfo(object):
    def __init__(self, webCrawler, crawlUrl):
        self.webCrawler = webCrawler
        self.crawlUrl = crawlUrl
        urlStatus = str(self.webCrawler.SetDriverUrl(crawlUrl))
        crawlerStatus = str(self.webCrawler.GetDriverStatus())
        msg = "web driver status: " + crawlerStatus + " url status: " + urlStatus
        LogManager.PrintLogMessage("CrawlBasicInfo", "__init__", msg, DefineManager.LOG_LEVEL_INFO)

    def CrawlCompanyName(self):
        try:
            webDriver = self.webCrawler.GetDriver()
            companyElements = webDriver.find_element_by_class_name(DefineManager.COMPANY_INFO_ELEMENTS_CLASS_NAME)
            companyName = companyElements.find_element_by_tag_name("a").text
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlCompanyName", "crawl company name successfully: " + companyName, DefineManager.LOG_LEVEL_INFO)
            return companyName
        except:
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlCompanyName", "crawl company name failed", DefineManager.LOG_LEVEL_ERROR)
        return None

    def CrawlCompanyStockCode(self):
        try:
            webDriver = self.webCrawler.GetDriver()
            companyElements = webDriver.find_element_by_class_name(DefineManager.COMPANY_INFO_ELEMENTS_CLASS_NAME)
            companyStockCode = companyElements.find_element_by_class_name("code").text
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlCompanyStockCode", "crawl company code successfully: " + companyStockCode, DefineManager.LOG_LEVEL_INFO)
            return companyStockCode
        except:
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlCompanyStockCode", "crawl company code failed", DefineManager.LOG_LEVEL_ERROR)
        return None

    def CrawlStockPrice(self):
        try:
            webDriver = self.webCrawler.GetDriver()
            stockElements = webDriver.find_element_by_class_name(DefineManager.STOCK_PRICE_ELEMENTS_CLASS_NAME)
            stockPrice = stockElements.find_element_by_class_name(DefineManager.STOCK_NUMBER_CLASS_NAME)
            stockPriceNumberElements = stockPrice.find_elements_by_tag_name(DefineManager.TAG_SPAN)

            stockPriceStr = ""
            for indexOfSpanNumber in stockPriceNumberElements:
                stockPriceStr = stockPriceStr + indexOfSpanNumber.text

            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlStockPrice", "crawl stock price successfully: " + stockPriceStr, DefineManager.LOG_LEVEL_INFO)

            return stockPriceStr
        except:
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlStockPrice", "crawl stock price failed", DefineManager.LOG_LEVEL_ERROR)
        return None

    def CrawlHighestStockPrice(self):
        try:
            webDriver = self.webCrawler.GetDriver()
            highLowPriceTable = webDriver.find_element_by_class_name(DefineManager.STOCK_HIGH_LOW_PRICE_INFO_TABLE)
            highPriceTableRow = highLowPriceTable.find_elements_by_tag_name(DefineManager.TAG_TR)[DefineManager.HIGHEST_PRICE_SAVED_ROW_POINT]
            highPriceTableCol = highPriceTableRow.find_elements_by_tag_name(DefineManager.TAG_TD)[DefineManager.HIGHEST_PRICE_SAVED_COL_POINT]
            highPrice = highPriceTableCol.find_element_by_class_name(DefineManager.STOCK_HIGH_NUMBER_CLASS_NAME)
            highPriceNumberElements = highPrice.find_elements_by_tag_name(DefineManager.TAG_SPAN)

            highPriceStr = ""
            for indexOfSpanNumber in highPriceNumberElements:
                highPriceStr = highPriceStr + indexOfSpanNumber.text

            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlHighestStockPrice", "crawl highest stock price successfully: " + highPriceStr, DefineManager.LOG_LEVEL_INFO)

            return highPriceStr
        except:
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlStockHighestPrice", "crawl highest stock price failed", DefineManager.LOG_LEVEL_ERROR)
        return None

    def CrawlLowestStockPrice(self):
        try:
            webDriver = self.webCrawler.GetDriver()
            highLowPriceTable = webDriver.find_element_by_class_name(DefineManager.STOCK_HIGH_LOW_PRICE_INFO_TABLE)
            lowPriceTableRow = highLowPriceTable.find_elements_by_tag_name(DefineManager.TAG_TR)[DefineManager.LOWEST_PRICE_SAVED_ROW_POINT]
            lowPriceTableCol = lowPriceTableRow.find_elements_by_tag_name(DefineManager.TAG_TD)[DefineManager.LOWEST_PRICE_SAVED_COL_POINT]
            lowPrice = lowPriceTableCol.find_element_by_class_name(DefineManager.STOCK_LOW_NUMBER_CLASS_NAME)
            lowPriceNumberElements = lowPrice.find_elements_by_tag_name(DefineManager.TAG_SPAN)

            lowPriceStr = ""
            for indexOfSpanNumber in lowPriceNumberElements:
                lowPriceStr = lowPriceStr + indexOfSpanNumber.text

            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlLowestStockPrice", "crawl lowest stock price successfully: " + lowPriceStr, DefineManager.LOG_LEVEL_INFO)

            return lowPriceStr
        except:
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlLowestStockPrice", "crawl lowest stock price failed", DefineManager.LOG_LEVEL_ERROR)
        return None

    def CrawlBestYearPrice(self):
        try:
            webDriver = self.webCrawler.GetDriver()
            sideTab = webDriver.find_element_by_class_name(DefineManager.STOCK_SIDE_TAB_CLASS_NAME)
            investmentOpinionSection = sideTab.find_element_by_class_name(DefineManager.STOCK_INVESTMENT_OPINION_CLASS_NAME)
            investmentOpinionRow = investmentOpinionSection.find_elements_by_tag_name(DefineManager.TAG_TR)[DefineManager.BEST_PRICE_OF_THE_YEAR_ROW_POINT]
            investmentOpinionCols = investmentOpinionRow.find_elements_by_tag_name(DefineManager.TAG_EM)

            bestPriceOfTheYear = investmentOpinionCols[DefineManager.BEST_PRICE_OF_THE_YEAR_COL_POINT].text

            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlBestYearPrice", "crawl best price of the year successfully: " + bestPriceOfTheYear, DefineManager.LOG_LEVEL_INFO)

            return bestPriceOfTheYear
        except:
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlBestYearPrice", "crawl best price of the year failed", DefineManager.LOG_LEVEL_ERROR)
        return None

    def CrawlWorstYearPrice(self):
        try:
            webDriver = self.webCrawler.GetDriver()
            sideTab = webDriver.find_element_by_class_name(DefineManager.STOCK_SIDE_TAB_CLASS_NAME)
            investmentOpinionSection = sideTab.find_element_by_class_name(
                DefineManager.STOCK_INVESTMENT_OPINION_CLASS_NAME)
            investmentOpinionRow = investmentOpinionSection.find_elements_by_tag_name(DefineManager.TAG_TR)[
                DefineManager.BEST_PRICE_OF_THE_YEAR_ROW_POINT]
            investmentOpinionCols = investmentOpinionRow.find_elements_by_tag_name(DefineManager.TAG_EM)

            worstPriceOfTheYear = investmentOpinionCols[DefineManager.WORST_PRICE_OF_THE_YEAR_COL_POINT].text

            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlWorstYearPrice",
                                       "crawl worst price of the year successfully: " + worstPriceOfTheYear,
                                       DefineManager.LOG_LEVEL_INFO)

            return worstPriceOfTheYear
        except:
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlWorstYearPrice", "crawl worst price of the year failed",
                                       DefineManager.LOG_LEVEL_ERROR)
        return None

    def CrawlDividendYield(self):
        try:
            webDriver = self.webCrawler.GetDriver()
            sideTab = webDriver.find_element_by_class_name(DefineManager.STOCK_SIDE_TAB_CLASS_NAME)
            perEpsTable = sideTab.find_element_by_class_name(
                DefineManager.STOCK_PER_EPS_CLASS_NAME)
            dividendYieldRow = perEpsTable.find_elements_by_tag_name(DefineManager.TAG_TR)[DefineManager.DIVIDEND_YIELD_ROW_POINT]
            dividendYieldPersent = dividendYieldRow.find_element_by_id(DefineManager.STOCK_DIVIDEND_YIELD_ID_NAME).text

            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlDividendYield", "crawl dividend yield successfully: " + dividendYieldPersent, DefineManager.LOG_LEVEL_INFO)

            return dividendYieldPersent
        except:
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlDividendYield", "crawl dividend yield failed", DefineManager.LOG_LEVEL_ERROR)

        return None

    def CrawlPriceChangedPercent(self):
        try:
            webDriver = self.webCrawler.GetDriver()
            stockElements = webDriver.find_element_by_class_name(DefineManager.STOCK_PRICE_ELEMENTS_CLASS_NAME)
            priceChangedPercent = stockElements.find_elements_by_tag_name(DefineManager.TAG_EM)[DefineManager.CHANGED_PRICE_PERCENT_SAVED_POINT]
            priceChangedPercentNumberElements = priceChangedPercent.find_elements_by_tag_name(DefineManager.TAG_SPAN)

            priceChangedPercentStr = ""
            for indexOfElement in priceChangedPercentNumberElements:
                priceChangedPercentStr = priceChangedPercentStr + indexOfElement.text
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlPriceChangedPercent", "crawl price changed percent successfully: " + priceChangedPercentStr, DefineManager.LOG_LEVEL_INFO)

            return priceChangedPercentStr
        except:
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlPriceChangedPercent", "crawl price changed percent failed", DefineManager.LOG_LEVEL_ERROR)

        return None

    def CrawlMarketCapitalization(self):
        try:
            webDriver = self.webCrawler.GetDriver()
            marketCapitalizationTable = webDriver.find_element_by_class_name(DefineManager.MARKET_CAPITALIZATION_CLASS_NAME)
            marketCapitalizationStr = marketCapitalizationTable.find_element_by_tag_name(DefineManager.TAG_TD).text

            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlMarketCapitalization", "crawl market capitalization successfully: " + marketCapitalizationStr, DefineManager.LOG_LEVEL_INFO)

            return marketCapitalizationStr
        except:
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlMarketCapitalization", "crawl market capitalization failed", DefineManager.LOG_LEVEL_ERROR)

        return None

    def CrawlYearBeta(self):
        try:
            webDriver = self.webCrawler.GetDriver()
            tabSubMenu = webDriver.find_element_by_class_name(DefineManager.STOCK_TAB_SUB_MENUS_CLASS_NAME)
            menuItems = tabSubMenu.find_elements_by_tag_name(DefineManager.TAG_A)
            self.webCrawler.ClickElement(menuItems[DefineManager.ITEM_ANALYSIS_POINT])

            subHtmlIframe = webDriver.find_element_by_id("coinfo_cp")
            webDriver = self.webCrawler.SwitchToFrame(subHtmlIframe)

            priceQuoteTable = webDriver.find_element_by_id(DefineManager.STOCK_QUOTE_TABLE_ID_NAME)
            yearBetaRow = priceQuoteTable.find_elements_by_tag_name(DefineManager.TAG_TR)[DefineManager.YEAR_BETA_ROW_POINT]
            yearBetaStr = yearBetaRow.find_element_by_tag_name(DefineManager.TAG_TD).text

            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlYearBeta", "crawl year beta successfully: " + yearBetaStr, DefineManager.LOG_LEVEL_INFO)

            webDriver = self.webCrawler.SwitchToDefault()
            tabSubMenu = webDriver.find_element_by_class_name(DefineManager.STOCK_TAB_SUB_MENUS_CLASS_NAME)
            menuItems = tabSubMenu.find_elements_by_tag_name(DefineManager.TAG_A)
            self.webCrawler.ClickElement(menuItems[DefineManager.TOTAL_INFO_POINT])

            return yearBetaStr
        except:
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlYearBeta", "crawl year beta failed", DefineManager.LOG_LEVEL_ERROR)

        return None

    def CrawlPER(self):
        try:
            webDriver = self.webCrawler.GetDriver()
            tabSubMenu = webDriver.find_element_by_class_name(DefineManager.STOCK_TAB_SUB_MENUS_CLASS_NAME)
            menuItems = tabSubMenu.find_elements_by_tag_name(DefineManager.TAG_A)
            self.webCrawler.ClickElement(menuItems[DefineManager.ITEM_ANALYSIS_POINT])

            subHtmlIframe = webDriver.find_element_by_id("coinfo_cp")
            webDriver = self.webCrawler.SwitchToFrame(subHtmlIframe)

            fundamentalTable = webDriver.find_element_by_class_name(DefineManager.FUNDAMENTAL_TABLE_CLASS_NAME)
            fundamentalRows = fundamentalTable.find_elements_by_tag_name(DefineManager.TAG_TR)
            fundamentalPerRow = fundamentalRows[DefineManager.FUNDAMENTAL_PER_ROW_POINT]
            fundamentalPerStr = fundamentalPerRow.find_elements_by_tag_name(DefineManager.TAG_TD)[DefineManager.TABLE_RIGHT_SIDE].text

            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlPER", "crawl PER successfully: " + fundamentalPerStr, DefineManager.LOG_LEVEL_INFO)

            webDriver = self.webCrawler.SwitchToDefault()
            tabSubMenu = webDriver.find_element_by_class_name(DefineManager.STOCK_TAB_SUB_MENUS_CLASS_NAME)
            menuItems = tabSubMenu.find_elements_by_tag_name(DefineManager.TAG_A)
            self.webCrawler.ClickElement(menuItems[DefineManager.TOTAL_INFO_POINT])

            return fundamentalPerStr
        except:
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlPER", "crawl PER failed", DefineManager.LOG_LEVEL_ERROR)

        return None

    def CrawlPBR(self):
        try:
            webDriver = self.webCrawler.GetDriver()
            tabSubMenu = webDriver.find_element_by_class_name(DefineManager.STOCK_TAB_SUB_MENUS_CLASS_NAME)
            menuItems = tabSubMenu.find_elements_by_tag_name(DefineManager.TAG_A)
            self.webCrawler.ClickElement(menuItems[DefineManager.ITEM_ANALYSIS_POINT])

            subHtmlIframe = webDriver.find_element_by_id("coinfo_cp")
            webDriver = self.webCrawler.SwitchToFrame(subHtmlIframe)

            fundamentalTable = webDriver.find_element_by_class_name(DefineManager.FUNDAMENTAL_TABLE_CLASS_NAME)
            fundamentalRows = fundamentalTable.find_elements_by_tag_name(DefineManager.TAG_TR)
            fundamentalPbrRow = fundamentalRows[DefineManager.FUNDAMENTAL_PBR_ROW_POINT]
            fundamentalPbrStr = fundamentalPbrRow.find_elements_by_tag_name(DefineManager.TAG_TD)[DefineManager.TABLE_RIGHT_SIDE].text

            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlPBR", "crawl PBR successfully: " + fundamentalPbrStr, DefineManager.LOG_LEVEL_INFO)

            webDriver = self.webCrawler.SwitchToDefault()
            tabSubMenu = webDriver.find_element_by_class_name(DefineManager.STOCK_TAB_SUB_MENUS_CLASS_NAME)
            menuItems = tabSubMenu.find_elements_by_tag_name(DefineManager.TAG_A)
            self.webCrawler.ClickElement(menuItems[DefineManager.TOTAL_INFO_POINT])

            return fundamentalPbrStr
        except:
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlPBR", "crawl PBR failed", DefineManager.LOG_LEVEL_ERROR)

        return None

    def CrawlEPS(self):
        try:
            webDriver = self.webCrawler.GetDriver()
            tabSubMenu = webDriver.find_element_by_class_name(DefineManager.STOCK_TAB_SUB_MENUS_CLASS_NAME)
            menuItems = tabSubMenu.find_elements_by_tag_name(DefineManager.TAG_A)
            self.webCrawler.ClickElement(menuItems[DefineManager.ITEM_ANALYSIS_POINT])

            subHtmlIframe = webDriver.find_element_by_id("coinfo_cp")
            webDriver = self.webCrawler.SwitchToFrame(subHtmlIframe)

            fundamentalTable = webDriver.find_element_by_class_name(DefineManager.FUNDAMENTAL_TABLE_CLASS_NAME)
            fundamentalRows = fundamentalTable.find_elements_by_tag_name(DefineManager.TAG_TR)
            fundamentalEpsRow = fundamentalRows[DefineManager.FUNDAMENTAL_EPS_ROW_POINT]
            fundamentalEpsStr = fundamentalEpsRow.find_elements_by_tag_name(DefineManager.TAG_TD)[DefineManager.TABLE_RIGHT_SIDE].text

            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlPBR", "crawl EPS successfully: " + fundamentalEpsStr, DefineManager.LOG_LEVEL_INFO)

            webDriver = self.webCrawler.SwitchToDefault()
            tabSubMenu = webDriver.find_element_by_class_name(DefineManager.STOCK_TAB_SUB_MENUS_CLASS_NAME)
            menuItems = tabSubMenu.find_elements_by_tag_name(DefineManager.TAG_A)
            self.webCrawler.ClickElement(menuItems[DefineManager.TOTAL_INFO_POINT])

            return fundamentalEpsStr
        except:
            LogManager.PrintLogMessage("CrawlBasicInfo", "CrawlPBR", "crawl EPS failed", DefineManager.LOG_LEVEL_ERROR)

        return None

    def __del__(self):
        return