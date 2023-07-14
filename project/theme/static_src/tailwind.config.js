/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
  content: [
    /**
     * HTML. Paths to Django template files that will contain Tailwind CSS classes.
     */

    /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
    "../templates/**/*.html",
    "../**/templates/**/*.html",

    /*
     * Main templates directory of the project (BASE_DIR/templates).
     * Adjust the following line to match your project structure.
     */
    "../../templates/**/*.html",

    /*
     * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
     * Adjust the following line to match your project structure.
     */
    "../../**/templates/**/*.html",

    /**
     * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
     * patterns match your project structure.
     */
    /* JS 1: Ignore any JavaScript in node_modules folder. */
    // '!../../**/node_modules',
    /* JS 2: Process all JavaScript files in the project. */
    // '../../**/*.js',

    /**
     * Python: If you use Tailwind CSS classes in Python, uncomment the following line
     * and make sure the pattern below matches your project structure.
     */
    // '../../**/*.py'
  ],
  theme: {
    extend: {
      colors: {
        "chartreuse": {
          50: "#e3e5e1",

          100: "#c8cdc4",

          200: "#aeb5a7",

          300: "#949d8c",

          400: "#7b8571",

          500: "#656e5d",

          600: "#51584a",

          700: "#3e4339",

          800: "#2a2e27",

          900: "#181a16",

        },
        "spring_green": {
          50: "#e2e6e4",

          100: "#c4cdc9",

          200: "#a8b6af",

          300: "#8d9e96",

          400: "#72877c",

          500: "#5f7067",

          600: "#4c5953",

          700: "#39433e",

          800: "#272e2b",

          900: "#161a18",

        },
        "cyan": {
          50: "#e1e5e5",

          100: "#c4cdcd",

          200: "#a8b6b6",

          300: "#8c9d9d",

          400: "#728686",

          500: "#5d6e6e",

          600: "#4c5959",

          700: "#394343",

          800: "#272e2e",

          900: "#161a1a",

        },
        "blue": {
          50: "#e5e5e9",

          100: "#cacad2",

          200: "#b1b1bd",

          300: "#9999a8",

          400: "#818195",

          500: "#6b6b7e",

          600: "#555564",

          700: "#40404b",

          800: "#2b2b33",

          900: "#19191e",

        },
        "violet": {
          50: "#e7e5e9",

          100: "#cdc9d1",

          200: "#b6b0bd",

          300: "#9f97a7",

          400: "#887f92",

          500: "#71687b",

          600: "#5b5362",

          700: "#443e4a",

          800: "#2f2b33",

          900: "#1b191d",

        },
        "rose": {
          50: "#e8e3e6",

          100: "#d1c9cd",

          200: "#bcafb6",

          300: "#a6969e",

          400: "#917e87",

          500: "#796670",

          600: "#605158",

          700: "#493e43",

          800: "#332b2f",

          900: "#1d191b",

        },
        "red": {
          50: "#e9e5e5",

          100: "#d1c9c9",

          200: "#bcafaf",

          300: "#a79797",

          400: "#927e7e",

          500: "#7b6868",

          600: "#625353",

          700: "#493e3e",

          800: "#332b2b",

          900: "#1d1919",

        },
        "yellow": {
          50: "#e5e5e1",

          100: "#ccccc3",

          200: "#b3b3a5",

          300: "#9c9c8a",

          400: "#848470",

          500: "#6c6c5b",

          600: "#565649",

          700: "#414137",

          800: "#2d2d26",

          900: "#191915",

        },
      }
    },
  },
  plugins: [
    /**
     * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
     * for forms. If you don't like it or have own styling for forms,
     * comment the line below to disable '@tailwindcss/forms'.
     */
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
    require("@tailwindcss/line-clamp"),
    require("@tailwindcss/aspect-ratio"),
  ],
};
