document.addEventListener("DOMContentLoaded", () => {
    console.log("Index page loaded");
    document.querySelector("#create_account").onclick = () => render_creation_page();
    document.querySelector("#log_in").onclick = () => render_login_page()
    if (document.querySelector("#state").value === "creation_form") {
        render_creation_page()
    } else if (document.querySelector("#state").value === "login") {
        render_login_page()
    }
})

function render_creation_page() {
    console.log("Rendering creation of profile page");
    document.querySelector("#creation_form").style.display = "block";
    document.querySelector("#login_form").style.display = "none"
    document.querySelector("#confirm_password").oninput = () => {
        document.querySelector("#password_warning").style.display = "block"
        if (document.querySelector("#password").value !== document.querySelector("#confirm_password").value) {
            // Do nothing
        } else {
            document.querySelector("#password_warning").style.display = "none"
        }
    }
}

function render_login_page() {
    console.log("Rendering creation of login page");
    document.querySelector("#login_form").style.display = "block";
    document.querySelector("#creation_form").style.display = "none";
}