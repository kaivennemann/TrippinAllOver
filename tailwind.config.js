

module.exports = {
  content: ["./src/website/booking/**/*.{html,js}"],
  theme: {
    extend: {},
    colors: {
      transparent: 'transparent',
      current: 'currentColor',
      'white': '#ffffff',
      'purple': '#3f3cbb',
      'navy-blue': '#100740',
      'silver': '#a3a3a3',
      'gray': '#cbd5e1',
      'dark-gray': '#4b5563',
      'light-gray': '#f9fafb',
      'light-black': '#111827',
      'blue': '#1d4ed8',
    },
    borderRadius: {
        DEFAULT: '4px',
        'lg': '0.5rem',
        'large': '12px',
    },
  },
  plugins: [],
}
