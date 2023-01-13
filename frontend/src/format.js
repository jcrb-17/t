export default function format(v) {
    function format1(index, v, string) {
        let temp = "";
        for (let i = 0; i < index - v.length; i++) {
            temp += string[i];
        }
        return temp;
    }
    function format2(index, v, string) {
        let temp = "";
        for (let i = index; i < string.length; i++) {
            temp += string[i];
        }
        return temp;
    }
    //format
    let items = document.getElementsByClassName("itemContent");

    for (let i = 0; i < items.length; i++) {
        const regex = new RegExp(`${v}`, "ig");
        let reg = regex.exec(items[i].textContent);
        if (reg != null || reg != undefined) {
            items[i].innerHTML = format1(regex.lastIndex, v, items[i].textContent)
                + `<f>${v}</f>`
                + format2(regex.lastIndex, v, items[i].textContent);
        }

    }
}