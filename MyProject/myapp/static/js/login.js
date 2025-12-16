function showSignupForm() {
    document.getElementById('login-form').style.display = 'none';
    document.getElementById('signup-form').style.display = 'block';
}
function showLoginForm() {
    document.getElementById('signup-form').style.display = 'none';
    document.getElementById('login-form').style.display = 'block';
}
function generateOTP() {
    const phone = document.getElementById('phone').value;
    if (phone.length < 10) {
        alert("Please enter a valid phone number.");
        return;
    }
    let otp = Math.floor(100000 + Math.random() * 900000);
    alert("Your OTP is: " + otp); // Simulating SMS sending
    document.getElementById('otp-field').style.display = 'block';
}