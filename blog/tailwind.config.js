/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./content/templates/**/*.html'],
  theme: {
    extend: {
      fontFamily: {
        charter: ['Charter', 'Bitstream Charter', 'Sitka Text', 'Cambria', 'serif'],
      },
    },
  },
  plugins: [],
}