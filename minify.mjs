import { readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import { minify as minifyHtml } from "html-minifier-terser";
import { transform } from "lightningcss";
import { minify as minifyJs } from "terser";

const dist = path.resolve("dist");

for (const name of ["index.html", "tos.html", "pp.html", "404.html"]) {
  const file = path.join(dist, name);
  const out = await minifyHtml(readFileSync(file, "utf8"), {
    collapseWhitespace: true,
    removeComments: true,
    removeRedundantAttributes: true,
    removeScriptTypeAttributes: true,
    removeStyleLinkTypeAttributes: true,
    collapseBooleanAttributes: true,
    useShortDoctype: true,
  });
  writeFileSync(file, out.replace(/\s*\n\s*/g, " "));
}

const cssFile = path.join(dist, "style.css");
const css = transform({
  filename: "style.css",
  code: readFileSync(cssFile),
  minify: true,
});
writeFileSync(cssFile, css.code.toString().replace(/\n/g, ""));

const jsFile = path.join(dist, "k.js");
const js = await minifyJs(readFileSync(jsFile, "utf8"), { compress: true, mangle: true });
writeFileSync(jsFile, js.code.replace(/\n/g, ""));
