import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from sdamgia import SdamGIA
from selenium.webdriver.edge.service import Service
from webdriver_manager import microsoft

DEV_MODE = False

url = input("Enter the URL: ")

driver = webdriver.Edge(service=Service(microsoft.EdgeChromiumDriverManager().install()))
# driver = webdriver.Edge(service=Service(executable_path="driver/msedgedriver.exe"))
driver.get(url=url)

sdamgia = SdamGIA()

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
tasks = soup.find_all('div', class_='titleTask')
answers = []
for num, task in enumerate(tasks):
    t = [i for i in task.p.strings][0][2:-1]
    z = sdamgia.get_problem_by_id('math', t)
    try:
        answers.append(z['answer'])
    except:
        answers.append('')

    print("Parsing tasks: " + str(num) + " of " + str(len(tasks)) + " done...")

    if DEV_MODE:
        break

driver.execute_script('''
    document.tasks = document.getElementsByClassName("task");
    document.showall = false;
    document.answerEls = [];
    ''')

for i in range(len(answers)):
    ans = str(answers[i])
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

driver.execute_script('''
    var btn = document.createElement("button");
    document.getElementsByTagName("body")[0].appendChild(btn)
    btn.innerHTML = "SHOW/HIDE ALL"
    btn.style.position = "fixed"
    btn.style.width = "10%"
    btn.style.height = "5%"
    btn.style.backgroundColor = "#ff957c"
    btn.onclick = ()=>{
        document.showall = !document.showall;
        document.answerEls.forEach((el)=>{
            if(el.style.backgroundColor != "white")
                el.style.backgroundColor = "white"
            else
                el.style.backgroundColor = "black"
        })
    }
    ''')

print("Done!")
while input("Type \'q\' to quit: ") != 'q':
    pass

# html = soup.prettify('utf-8')
# with open("output.html", "wb") as file:
#    file.write(html)
