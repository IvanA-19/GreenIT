function full_text(data, num) {
    let current_text = document.getElementById(`module_${num}_text`).innerText;

    document.getElementById(`module_${num}_text`).innerText = data;
    console.log(document.getElementById(`module_${num}_text`));
    let hide_button = document.getElementById(`hide_${num}`);

    hide_button.innerHTML += `<button class="btn btn-lg btn-success" id="button_${num}">Скрыть</button>`;

    document.getElementById(`show_button_${num}`).style.visibility = 'hidden';

    let button = document.getElementById(`button_${num}`);

    button.onclick = () => {
        document.getElementById(`module_${num}_text`).innerText = current_text;
        button.remove();
        document.getElementById(`show_button_${num}`).style.visibility = 'visible';
    }
}
