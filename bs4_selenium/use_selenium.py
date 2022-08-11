from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller

def make_web_driver(): # selenium 전용 자동화 Chrome 설정
    path = chromedriver_autoinstaller.install()                             #[질문] 무엇을 설치하는거징? 크롬드라이버의 바이너리파일위치 경로?? 
                                                                            # 셀레니움이 쓰는 크롬은 내가 쓰는 크롬과 다름. 
    options = webdriver.ChromeOptions()                                     # 옵션설정값들을 options 변수에 넣고 변경한다.
    options.add_argument("start-maximized")                                 # options- 창 최대화된 상태로 크롬 실행
    options.add_argument('--disable-blink-features=AutomationControlled')   
        # ↑ navigator.webdriver라는 속성이 "user가 봇인지 아닌지 [참],[거짓]으로 알려줌" https://dev.to/composite/-50a1 [참고]
        # 근데 위처럼 옵션 지정하면 크롬드라이버 실행할때 webdriver=true 표시되지않게 함. https://stackoverflow.com/a/60409220 [참고]
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
        # ↑ 위 두 옵션 또한 셀레늄 봇질 뚫기 옵션추가요소로 추정 https://dev.to/composite/-50a1 [참고]
    driver = webdriver.Chrome(options=options, service=Service(path))       # webdriver.Chrome()함수는 크롬인스턴스(프로세스) 실행 [질문]옵션은 알겠는데 service는 뭐지
    driver.implicitly_wait(10)                                              # 어떤 속성이 발견되기까지 10초 기다림 10초 지나면 timeout 근데 이전에 나타나면 wait 종료.[질문] 무슨속성을 기다리는중?
    return driver                                                           # 웹드라이버 객체 반환 [느낌상 크롬창 1개 만들고 그 객체를 반환하는 듯]