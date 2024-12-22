from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class FindPlacePage(BasePage):
    page_name = "Find Place Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "find_place_locator")
    lbl_property_finder = Label(locator_reader, "lbl_property_finder")
    lbl_dubizzle = Label(locator_reader, "lbl_dubizzle")
    lbl_bayut = Label(locator_reader, "lbl_bayut")

    def __init__(self):
        super(FindPlacePage, self).__init__(self.page_element)

    def is_property_finder_present(self):
        return self.lbl_property_finder.is_present() and self.lbl_property_finder.is_displayed()

    def is_dubizzle_present(self):
        return self.lbl_dubizzle.is_present() and self.lbl_dubizzle.is_displayed()

    def is_bayut_present(self):
        return self.lbl_bayut.is_present() and self.lbl_bayut.is_displayed()



    


