import use_selenium as us # use_selenium.py를 땡겨옴(라이브러리 아님!)
import elem_selectors as es # elem_selectors.py를 땡겨옴(라이브러리 아님!)
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

target_url = "https://www.nike.com/kr/ko_kr/"

def get_rocket_prod_list(): # 로켓 배송 상품리스트 가져오기
    driver = us.make_web_driver()           # 크롬창 1개 만들기.
    driver.get(target_url)                  # .get("주소문자열")함수는 해당세션에 주소 로딩하는함수
    time.sleep(1)                           # time.sleep(초) 1초대기
    driver.find_element(By.CSS_SELECTOR, es.MODAL_CLOSE_SELECTOR).click() 
    #driver.find_element(By.XPATH, es.MODAL_CLOSE_XPATH).click()
    time.sleep(1)
    driver.find_element(By.XPATH, es.MEMBERS_DAYS_XPATH).click()
    driver.implicitly_wait(10)

    # driver.find_element(무슨속성으로 찾을건지, 찾을 목표값).send_keys(입력할 문자, Keys.ENTER)
    # 무슨속성으로 찾을건지 아래: (css selector 문법 [참고] https://greenfishblog.tistory.com/193)
    """
        class By:
        Set of supported locator strategies.

        ID = "id"
        XPATH = "xpath"
        LINK_TEXT = "link text"
        PARTIAL_LINK_TEXT = "partial link text"
        NAME = "name"
        TAG_NAME = "tag name"
        CLASS_NAME = "class name"
        CSS_SELECTOR = "css selector"
    """
    page_html = BeautifulSoup(driver.page_source, 'html.parser') # 페이지 내에 있는 모든 코드를 html 파싱
    prod_page = page_html.select_one(es.PROD_LIST_SELECTOR)
    prod_all_items = prod_page.select(es.PROD_ITEM_SELECTOR)

    rocket_prod_list = []                   # 파이썬에서 list 정의
    for prod in prod_all_items:
        is_rocket = prod.get("data-is-rocket") #[로켓 배송] 태그가 있는 상품만 구분
        if is_rocket == 'true':
            prod_name = prod.select_one("div.descriptions-inner div.name").text
            print(prod_name.strip()) # strip()을 통해서 텍스트 앞뒤의 여백 제거
            rocket_prod_list.append(prod)   # append(데이터) => 리스트의 마지막에 데이터 추가
    return rocket_prod_list

get_rocket_prod_list()


