from bs4 import BeautifulSoup
from selenium import webdriver
from sdamgia import SdamGIA
from selenium.webdriver.edge.service import Service
from webdriver_manager import microsoft

import menu
from color import *

DEV_MODE = False


def runScript(file, driver):
    with open(file) as f:
        script = f.read()
        driver.execute_script(script)



if __name__ == "__main__":
    url = menu.getUrlChoice()
    print('Please wait.......')

    if DEV_MODE:
        url = "https://prof.mathege.ru/prototypes/?position=11&filter=&limit=1000"

    driver = webdriver.Edge(service=Service(microsoft.EdgeChromiumDriverManager().install()))
    # driver = webdriver.Edge(service=Service(executable_path="driver/msedgedriver.exe"))
    driver.get(url=url)
    driver.minimize_window()

    sdamgia = SdamGIA()

    soup = BeautifulSoup(driver.page_source, 'lxml')
    tasks = soup.find_all('div', class_='titleTask')
    answers = []
    for num, task in enumerate(tasks):
        try:
            t = [i for i in task.p.strings][0][2:-1]
            z = sdamgia.get_problem_by_id('math', t)
            try:
                answers.append(z['answer'])
            except:
                answers.append('')

            print(Fore.GREEN + "Parsing tasks: " + str(num) + " of " + str(len(tasks)) + " done..." + Style.RESETALL)

            if DEV_MODE:
                break
        except:
            print("Failed, moving on...")

    driver.execute_script('''
        document.tasks = document.getElementsByClassName("task");
        document.showall = false;
        document.answerEls = [];
        ''')

    for i in range(len(answers)):
        ans = str(answers[i])
        #append hover blocks
        driver.execute_script('''
        let ans = document.createElement("p")

        ans.style.backgroundColor = "black"
        ans.onmouseenter = ()=>{
            if(!document.showall)
                ans.style.backgroundColor = "white"
        }
        ans.onmouseleave = ()=>{
            if(!document.showall)
                ans.style.backgroundColor = "black"
        }

        document.tasks[''' + str(i) + '''].appendChild(ans)
        ans.innerHTML =  "Answer: ''' + str(ans) + '''"
        document.answerEls.push(ans)
        ''')
        if DEV_MODE:
            break

    #setup show/hide button
    runScript("btnSetup.js", driver)

    #setup handy next task
    runScript("control.js", driver)

    print("Done!")
    while input("Type \'q\' to quit: ") != 'q':
        pass
