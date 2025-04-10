import React from "react";
import clsx from "clsx";
import { translate } from "@docusaurus/Translate";
import Link from '@docusaurus/Link';
import Heading from "@theme/Heading";

export default function NotFoundContent({ className }) {
  return (
    <main className={clsx("container margin-vert--xl", className)}>
      <div className="row">
        <div className="col col--6 col--offset-3">
          <Heading as="h1" className="hero__title">
            {translate({
              id: "theme.NotFound.title",
              message: "Page Not Found",
              description: "The title of the 404 page"
            })}
          </Heading>
          <p>
            {translate({
              id: "theme.NotFound.p1",
              message: "We could not find what you were looking for.",
              description: "The first paragraph of the 404 page"
            })}
          </p>
          <p>
            Head back to our <Link to="/">main docs page</Link> or use the search bar to find the
            page you need.
          </p>
        </div>
      </div>
    </main>
  );
}
