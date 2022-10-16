function updateCurrentTask() {
	for(let element of document.tasks) {
        element.style.backgroundColor = "white"
    }
	document.tasks[document.currentTask].style.backgroundColor = "#adffb2";
	document.tasks[Math.max(document.currentTask-1),0].scrollIntoView(true);
}

document.currentTask = 0;
window.onkeydown = (e) => {
	if (e.key == " ") {
		document.currentTask += 1;
		updateCurrentTask();
	}
};
