/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html"],
  theme: {
    extend: {
      colors:{
        chatblack: {50: '#343541'},
        purple: {50: '#7c00b5'}
      }
    },
  },
  plugins: [],
}

