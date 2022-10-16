var btn = document.createElement("button");
document.getElementsByTagName("body")[0].appendChild(btn)
btn.innerHTML = "SHOW/HIDE ALL"
btn.style.position = "fixed"
btn.style.left = "30%"
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
