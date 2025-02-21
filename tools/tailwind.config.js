/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../forget_me_not_app/templates/forget_me_not_app/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [require('daisyui'),],
  daisyui: {
    themes: ["cupcake"],
  },
}
