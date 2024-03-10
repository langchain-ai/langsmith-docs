/* eslint-disable global-require,import/no-extraneous-dependencies */

// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion
// eslint-disable-next-line import/no-extraneous-dependencies

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "🦜️🛠️ LangSmith",
  tagline: "LangSmith",
  favicon: "img/favicon.ico",
  customFields: {},
  // Set the production url of your site here
  url: "https://smith.langchain.com/", // TODO: also make configurable with dev deployment
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: "/",
  trailingSlash: false,

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "throw",

  plugins: [
    [
      '@scalar/docusaurus',
      {
        label: 'LangSmith API Docs',
        route: '/api-docs',
        configuration: {
          spec: {
            url: 'https://api.smith.langchain.com/openapi.json',
          },
        },
      },
    ],
  ],

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
          remarkPlugins: [
            [require("@docusaurus/remark-plugin-npm2yarn"), { sync: true }],
          ],
          async sidebarItemsGenerator({
            defaultSidebarItemsGenerator,
            ...args
          }) {
            const sidebarItems = await defaultSidebarItemsGenerator(args);
            sidebarItems.forEach((subItem) => {
              // This allows breaking long sidebar labels into multiple lines
              // by inserting a zero-width space after each slash.
              if (
                "label" in subItem &&
                subItem.label &&
                subItem.label.includes("/")
              ) {
                // eslint-disable-next-line no-param-reassign
                subItem.label = subItem.label.replace(/\//g, "/\u200B");
              }
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
        disableSwitch: true,
        respectPrefersColorScheme: true,
      },
      prism: {
        theme: require("prism-react-renderer/themes/vsLight"),
        darkTheme: require("prism-react-renderer/themes/vsDark"),
      },
      image: "img/langsmith-logo.svg",
      navbar: {
        title: "🦜️🛠️ LangSmith Docs",
        items: [
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
          {
            type: "search",
            position: "right",
          },
          {
            href: "https://smith.langchain.com/",
            label: "Go to App",
            position: "right",
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
                label: "Discord",
                href: "https://discord.gg/cU2adEyC7w",
              },
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
                href: "https://github.com/langchain-ai/langsmith-docs"
              },
              {
                label: "LangSmith SDK",
                href: "https://github.com/langchain-ai/langsmith-sdk"

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
    scripts: [
      "/js/google_analytics.js",
      {
        src: "https://www.googletagmanager.com/gtag/js?id=G-62DTR64PQZ",
        async: true,
      },
    ],
};

module.exports = config;
