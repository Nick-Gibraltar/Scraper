import scraper
import unittest

class ScraperTestCase(unittest.TestCase):
        
    def test_scraper_class(self):
        data_collect = scraper.Scraper()
        self.assertEqual("https://www.screwfix.com/", data_collect.open_url())
        data_collect.cookies_check()
        self.assertEqual("https://www.screwfix.com/c/tools/squares/cat14550006?cm_sp=managedredirect-_-handtools-_-squares", data_collect.initial_search("set square"))
        self.assertEqual(0, len(data_collect.get_sub_category_list()))
        data_collect.get_sub_category_choice()
        self.assertEqual({'https://www.screwfix.com/p/dewalt-rafter-square-12-300mm/114ky',
                            'https://www.screwfix.com/p/dewalt-rafter-square-7-177mm/780ky',
                            'https://www.screwfix.com/p/magnusson-combination-square-2-pieces/5282v',
                            'https://www.screwfix.com/p/magnusson-combination-square-12-300mm/1219v',
                            'https://www.screwfix.com/p/magnusson-rafter-square-6-2-3-170mm/9652v',
                            'https://www.screwfix.com/p/bahco-combination-square-12-300mm/3870k',
                            'https://www.screwfix.com/p/magnusson-combination-square/3791v',
                            'https://www.screwfix.com/p/stanley-combination-square-12-300mm/33486',
                            'https://www.screwfix.com/p/magnusson-framing-square-16-x-24-405-x610mm/6641v',
                            'https://www.screwfix.com/p/magnusson-t-square-22-x-50-560-x1270mm/2057v',
                            'https://www.screwfix.com/p/bahco-combination-square-16-400mm/2795k',
                            'https://www.screwfix.com/p/stanley-rafter-square-6-3-4-171mm/1655f',
                            'https://www.screwfix.com/p/magnusson-framing-square-10-x-16-255-x410mm/3784v',
                            'https://www.screwfix.com/p/stanley-t-square-22-1-4-x-48-565-x1220mm/5826k',
                            'https://www.screwfix.com/p/bahco-combination-square-6-150mm/7045k',
                            'https://www.screwfix.com/p/forge-steel-carpenters-square-9-x-7-230mm-x-185mm/720xg',
                            'https://www.screwfix.com/p/faithfull-combination-square-12-300mm/917rk',
                            'https://www.screwfix.com/p/faithfull-quick-imperial-rafter-square-12-300mm/863rk',
                            'https://www.screwfix.com/p/faithfull-adjustable-quick-rafter-square-12-300mm/695rk',
                            'https://www.screwfix.com/p/faithfull-quick-imperial-rafter-square-7-180mm/705rk'},
                                    data_collect.get_product_links())

unittest.main(argv=['first-arg-is-ignored'], exit=False)