const bioSubmitButton = document.querySelectorAll(".submit")[0]
bioSubmitButton.addEventListener("click", async ()=>{
    const bio = document.querySelector("textarea[name='bio']").value;
    console.log(bio)
})
