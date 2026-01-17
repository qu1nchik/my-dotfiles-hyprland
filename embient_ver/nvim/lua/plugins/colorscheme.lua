return {
  -- TokyoNight тема
  {
    "folke/tokyonight.nvim",
    lazy = false, -- Загружаем сразу, так как это основная тема
    priority = 1000, -- Высокий приоритет для корректной загрузки
    config = function()
      require("tokyonight").setup({
        style = "moon", -- Варианты: "storm", "night", "moon"
        light_style = "day", -- Для светлого режима
        transparent = false, -- Прозрачный фон
        terminal_colors = true, -- Цвета для терминала
        styles = {
          comments = { italic = true },
          keywords = { italic = true },
        },
        -- Можно включить один из вариантов:
        sidebars = "dark", -- "dark", "transparent", "normal"
        -- day_brightness = 0.3, -- Яркость светлой темы
        -- hide_inactive_statusline = false,
      })

      -- Установка темы по умолчанию
      vim.cmd.colorscheme("tokyonight")
    end,
  },

  -- Альтернативные темы (закомментированы, раскомментируйте нужную)
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
