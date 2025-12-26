return {
  {
    "catppuccin/nvim",
    name = "catppuccin",
    opts = {
      flavour = "macchiato", -- mocha, macchiato, frappe, latte
      background = {
        light = "latte",
        dark = "mocha",
      },
    },
  },
  {
    "LazyVim/LazyVim",
    opts = {
      colorscheme = "catppuccin",
    },
  },
}
