from selene import browser, be, have


def test_should_text():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_should_not_text():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.no.text('qwerty'))


def test_should_text_ya():
    browser.open('https://ya.ru/')
    browser.element('[name="text"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search-result"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_should_not_text_ya():
    browser.open('https://ya.ru/')
    browser.element('[name="text"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search-result"]').should(have.no.text('qwerty'))


def test_should_text_duck():
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="react-layout"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_should_not_text_duck():
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="react-layout"]').should(have.no.text('qwerty'))


def test_empty_result():
    browser.open("https://google.ru")
    browser.element('[name="q"]').should(be.blank).type('razrazrazetoharbass').press_enter()
    browser.element('#botstuff').should(have.text('По запросу razrazrazetoharbass ничего не найдено.'))
