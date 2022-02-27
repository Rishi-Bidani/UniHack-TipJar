const bioSubmitButton = document.querySelectorAll(".submit")[0]
bioSubmitButton.addEventListener("click", async () => {
    const bio = document.querySelector("textarea[name='bio']").value;
    // send request to /user/code/edit - put

})


const addNewOption = document.querySelector(".add-new-payment");
const newElem = Object.assign(
    document.createElement("div"),
    {
        className: "form--container",
        innerHTML: `
                <select name="chooseTipMethod[]" required>
                    <option value="">--Select Option--</option>
                    <option value="eth">Ethereum</option>
                    <option value="btc">BitCoin</option>
                </select>
                <input type="text" name="link[]" placeholder="Your link">`
    }
)
addNewOption.addEventListener("click", () => {
    console.log(newElem)
    addNewOption.parentElement.querySelector("section").append(newElem.cloneNode(true))
})

document.querySelector("#links").addEventListener("submit", async (e)=>{
    e.preventDefault();
    // console.table([...data]);
    const rawData = [...new FormData(e.target)]
    const data = [];
    for(let i = 0; i < rawData.length - 1; i+=2){
        data.push([rawData[i][1], rawData[i+1][1]])
    }
    console.log(data)

    const action = e.target.getAttribute("action")
    const res = await fetch(action, {
        method: "PUT",
        body: JSON.stringify(data)
    })
})