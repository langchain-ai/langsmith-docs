/* eslint-disable global-require,import/no-extraneous-dependencies */
require("dotenv").config();

// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion
// eslint-disable-next-line import/no-extraneous-dependencies

const prism = require("prism-react-renderer");

const baseLightCodeBlockTheme = prism.themes.vsLight;
const baseDarkCodeBlockTheme = prism.themes.vsDark;

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "🦜️🛠️ LangSmith",
  tagline: "LangSmith",
  favicon: "img/favicon.png",
  customFields: {
    supabaseUrl: process.env.NEXT_PUBLIC_SUPABASE_URL,
    supabasePublicKey: process.env.NEXT_PUBLIC_SUPABASE_PUBLIC_KEY,
  },
  // Set the production url of your site here
  url: "https://docs.smith.langchain.com/", // TODO: also make configurable with dev deployment
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: "/",
  trailingSlash: false,

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "throw",

  markdown: {
    mermaid: true,
  },
  themes: ["@docusaurus/theme-mermaid"],

  plugins: [
    [
      "@docusaurus/plugin-google-tag-manager",
      {
        containerId: "GTM-WRT5MXDT",
      },
    ],
  ],

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          lastVersion: "current",
          versions: {
            current: {
              label: "stable",
              badge: false,
            },
          },
          sidebarPath: require.resolve("./sidebars.js"),
          remarkPlugins: [
            [require("@docusaurus/remark-plugin-npm2yarn"), { sync: true }],
          ],
          async sidebarItemsGenerator({
            defaultSidebarItemsGenerator,
            ...args
          }) {
            let sidebarItems = await defaultSidebarItemsGenerator(args);

            sidebarItems = sidebarItems.filter(
              (i) => !(i.type === "doc" && i.id.split("/").at(-1) === "index")
            );

            sidebarItems = sidebarItems.map((subItem) => {
              const newItem = { ...subItem };

              // This allows breaking long sidebar labels into multiple lines
              // by inserting a zero-width space after each slash.
              if (
                "label" in newItem &&
                newItem.label &&
                newItem.label.includes("/")
              ) {
                // eslint-disable-next-line no-param-reassign
                newItem.label = newItem.label.replace(/\//g, "/\u200B");
              }
              if (args.item.className) {
                newItem.className = args.item.className;
              }
              return newItem;
            });
            return sidebarItems;
          },
          routeBasePath: "/",
        },
        pages: {
          remarkPlugins: [require("@docusaurus/remark-plugin-npm2yarn")],
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      }),
    ],
  ],
  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        disableSwitch: false,
        respectPrefersColorScheme: true,
      },
      announcementBar: {
        content:
          'We are growing and hiring for multiple roles for LangChain, LangGraph and LangSmith. <a href="https://www.langchain.com/careers" target="_blank" rel="noopener noreferrer">Join our team!</a>',
      },
      prism: {
        theme: {
          ...baseLightCodeBlockTheme,
        },
        darkTheme: {
          ...baseDarkCodeBlockTheme,
        },
      },
      image: "img/langsmith-preview.png",
      navbar: {
        logo: {
          src: "img/langsmith-logo-black.svg",
          srcDark: "img/langsmith-logo-white.svg",
        },
        items: [
          {
            type: "search",
            position: "right",
          },
          {
            type: "custom-RegionSelector",
            position: "right",
          },
          {
            href: "https://smith.langchain.com/",
            label: "Go to App",
            position: "right",
          },
          {
            type: "dropdown",
            label: "API Reference",
            position: "left",
            items: [
              {
                label: "REST",
                href: "https://api.smith.langchain.com/redoc",
              },
              {
                label: "Python",
                to: "https://docs.smith.langchain.com/reference/python",
              },
              {
                label: "JS/TS",
                to: "https://docs.smith.langchain.com/reference/js",
              },
            ],
          },
        ],
      },
      footer: {
        style: "light",
        links: [
          {
            title: "Community",
            items: [
              {
                label: "Twitter",
                href: "https://twitter.com/LangChainAI",
              },
            ],
          },
          {
            title: "GitHub",
            items: [
              {
                label: "Docs Code",
                href: "https://github.com/langchain-ai/langsmith-docs",
              },
              {
                label: "LangSmith SDK",
                href: "https://github.com/langchain-ai/langsmith-sdk",
              },
              {
                label: "Python",
                href: "https://github.com/langchain-ai/langchain",
              },
              {
                label: "JS/TS",
                href: "https://github.com/langchain-ai/langchainjs",
              },
            ],
          },
          {
            title: "More",
            items: [
              {
                label: "Homepage",
                href: "https://langchain.com",
              },
              {
                label: "Blog",
                href: "https://blog.langchain.dev",
              },
              {
                href: "https://python.langchain.com/en/latest/",
                label: "LangChain Python Docs",
                position: "left",
              },
              {
                href: "https://js.langchain.com/docs/",
                label: "LangChain JS/TS Docs",
                position: "left",
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} LangChain, Inc.`,
      },
      algolia: {
        // The application ID provided by Algolia
        appId: "HUOFIK2DR9",

        // Public API key: it is safe to commit it
        // this is linked to erick@langchain.dev currently
        apiKey: "a338e3c2aefa362c6a245b747c7112df",

        indexName: "smith-langchain",

        contextualSearch: true,
      },
    }),
  scripts: [],
};

module.exports = config;
