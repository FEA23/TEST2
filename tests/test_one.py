import time
from pages.element_page import TextBoxPage, CheckBoxPage, RadioButtonPage





class TestElements:
    class TestTextBox:

        def test(self, driver):
            text_box = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box.open()
            input_data = text_box.fill_all_fields()
            output_data = text_box.check_filled_form()
            assert input_data == output_data

    class TestCheckBox:
        def test_check_box(self,driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            #check_box_page.get_checked_checkbox()

    class TestRadioButton:

        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes'
            assert output_impressive == 'Impressive'
            assert output_no == 'No', '"No" have not been selected'