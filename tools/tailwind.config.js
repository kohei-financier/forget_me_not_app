/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../forget_me_not_app/templates/forget_me_not_app/*.html",
    "../users/templates/registration/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("@tailwindcss/typography"), require("daisyui")],
  daisyui: {
    themes: ["light"],
  },
}
