return {
  -- GRUVBOX NEOVIM
  {
    "ellisonleao/gruvbox.nvim",
    priority = 1000,
    lazy = false,
    opts = {},
    config = function(_, opts)
      require("gruvbox").setup(opts)
      vim.cmd.colorscheme("gruvbox")
    end,
  },

  -- ATOMIC NEOVIM
  -- "kurund/atomic.nvim",
  -- lazy = false,
  -- priority = 1000,
  -- config = function()
  -- vim.cmd.colorscheme("atomic")
  -- end,

  -- CATPPUCCIN NEOVIM
  -- {
  --   "catppuccin/nvim",
  --   name = "catppuccin",
  --   lazy = false,
  --   priority = 1000,
  --   config = function()
  --     require("catppuccin").setup({
  --       flavour = "macchiato", -- latte, frappe, macchiato, mocha
  --       background = {
  --         light = "latte",
  --         dark = "mocha",
  --       },
  --     })
  --     vim.cmd.colorscheme("catppuccin")
  --   end,
  -- },

  -- {
  --   "navarasu/onedark.nvim",
  --   lazy = false,
  --   priority = 1000,
  --   config = function()
  --     require("onedark").setup({
  --       style = "dark", -- dark, darker, cool, deep, warm, warmer, light
  --     })
  --     vim.cmd.colorscheme("onedark")
  --   end,
  -- },

  -- {
  --   "Mofiqul/dracula.nvim",
  --   lazy = false,
  --   priority = 1000,
  --   config = function()
  --     vim.cmd.colorscheme("dracula")
  --   end,
  -- },

  -- {
  --   "ellisonleao/gruvbox.nvim",
  --   lazy = false,
  --   priority = 1000,
  --   config = function()
  --     require("gruvbox").setup({
  --       contrast = "hard", -- soft, medium, hard
  --     })
  --     vim.cmd.colorscheme("gruvbox")
  --   end,
  -- },

  -- {
  --   "rebelot/kanagawa.nvim",
  --   lazy = false,
  --   priority = 1000,
  --   config = function()
  --     require("kanagawa").setup({
  --       theme = "wave", -- wave, dragon, lotus
  --     })
  --     vim.cmd.colorscheme("kanagawa-wave")
  --   end,
  -- },

  -- {
  --   "rose-pine/neovim",
  --   name = "rose-pine",
  --   lazy = false,
  --   priority = 1000,
  --   config = function()
  --     require("rose-pine").setup({
  --       variant = "main", -- main, moon, dawn
  --     })
  --     vim.cmd.colorscheme("rose-pine")
  --   end,
  -- },
}
