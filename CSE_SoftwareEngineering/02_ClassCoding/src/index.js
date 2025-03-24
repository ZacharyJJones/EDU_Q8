import { data } from "../data/data.js";

// Render a to-do item

// todoContainer

function renderListItem(todoData) {
	const h3 = document.createElement("h3");
	h3.textContent = todoData.todo;

	const span = document.createElement("span");
	span.textContent = todoData.dueDate;

	const p = document.createElement("p");
	p.textContent = todoData.notes;

	const li = document.createElement("li");
	li.append(h3, span, p);

	return li;
}

const arrayOf_li = data.map((a) => renderListItem(a));

const ul = document.querySelector(".todoContainer");
arrayOf_li.forEach((element) => {
	ul.append(element);
});

// Handle form submission

const form = document.querySelector("form");

form.addEventListener("submit", (e) => {
	e.preventDefault();
	const newTodoData = {
		todo: e.target.todo.value,
		dueDate: e.target.dueDate.value,
		notes: e.target.notes.value,
	};

	ul.append(renderListItem(newTodoData));
});
