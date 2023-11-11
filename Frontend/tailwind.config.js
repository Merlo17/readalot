/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './templates/**/*.html',
        './templates/**/*.twig',
        './templates/**/*.vue',
        './src/**/*.js',
        './src/**/*.jsx',
        './src/**/*.ts',
        './src/**/*.vue',
    ],
    theme: {
        extend: {
            lineClamp: {
                24: '24',
            }
        },
    },
    plugins: [],
};
