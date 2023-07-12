import time
from pages.element_page import TextBoxPage



class TestElements:
    class TestTextBox:

        def test(self, driver):
            text_box = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box.open()
            input_data = text_box.fill_all_fields()
            output_data = text_box.check_filled_form()
            assert input_data == output_data