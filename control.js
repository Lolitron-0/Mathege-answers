function updateCurrentTask() {
	for (let i = 0; i < document.tasks.length; i++) {
		let element = document.tasks[i];
		element.style.backgroundColor = "white";
	}
	document.tasks[document.currentTask].style.backgroundColor = "#adffb2";
	document.tasks[Math.max(document.currentTask - 1, 0)].scrollIntoView({
		behavior: "smooth",
	});
}

document.currentTask = 0;
updateCurrentTask();
window.onkeydown = (e) => {
	if (e.key == "Shift") {
		document.currentTask += 1;
		updateCurrentTask();
	}
};
