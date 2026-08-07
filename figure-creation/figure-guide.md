# How to Make a Publication Figure
### A plain-English guide. No jargon. Follow the steps.
*Distilled from the NeurIPS, ICML, and ICLR style files and author instructions,
the canonical visualization literature (Rougier et al., Tufte, Borland & Taylor,
Crameri et al., Okabe & Ito), and the matplotlib and Figma documentation. Sibling
of `caption-writing/`: the figure and its caption ship as one exhibit, and this
guide hands off to that one at the end. Every venue number below is attributed to
the source it came from, with a URL, so the rules stay auditable.*

Throughout, one invented toy system carries the examples: **TileSort**, a
conveyor rig that sorts colored tiles into bins. Its three parts are the
**scanner** (photographs each tile as it passes), the **sorter** (predicts a bin
and drives the gripper), and the **reject chute** (diverts tiles the sorter
scores below a confidence threshold). Nothing about TileSort is real; it exists
only to make the templates concrete.
---

## Part 0: The terms you need, in plain words

| Fancy term | Plain meaning | Why it matters here |
|---|---|---|
| **Column width** | The exact printed width of the text block your figure sits in, in inches. | Build at this width and nothing gets rescaled. |
| **Vector vs raster** | Vector stores shapes (PDF, SVG, EPS); raster stores pixels (PNG, JPG). | Vector stays sharp at any zoom and keeps text as text. |
| **Font embedding** | The font's outlines are stored inside the PDF instead of assumed present. | A non-embedded font renders as something else on the reviewer's machine. |
| **Type 3 vs Type 42** | Two ways a PDF stores glyphs. Type 3 is a bitmap-ish legacy form; Type 42 is TrueType. | Some venues and arXiv flag or reject Type 3. |
| **Data-ink ratio** | The share of ink that encodes data rather than decoration (Tufte). | Raise it by deleting, not by adding. |
| **Chartjunk** | Ink that tells the viewer nothing new: 3D bevels, gradients, box frames, dense grids (Tufte). | Every deletion makes the claim louder. |
| **Small multiples** | The same small chart repeated across a varying condition (Tufte). | The cheapest way to show four conditions without four figures. |
| **Redundant encoding** | Every series distinguished by color *and* line style *and* marker. | The figure survives grayscale and color vision deficiency. |
| **Perceptually uniform colormap** | Equal steps in the data look like equal steps in color (viridis). | Rainbow maps invent edges the data does not have. |
| **Frame (Figma)** | A fixed-size container that is the exported artboard. | One frame per figure, sized to the column. |
| **Component (Figma)** | A master block you instance many times; editing the master edits all copies. | Repeated boxes in a pipeline diagram stay identical. |
| **Auto layout (Figma)** | Padding and spacing rules that reflow a frame's contents. | Consistent gutters without hand-nudging. |
| **rcParams (matplotlib)** | The global style dictionary set once at the top of a plotting script. | The whole figure family inherits one look. |

That is all the theory. Everything below is rules, numbers, and checklists.
---

## Part 1: Decide the figure's ONE job before you draw it

Write the claim first, as an English sentence, then build the smallest picture
that discharges it.

- **Rule 2 of "Ten Simple Rules for Better Figures" is "Identify your message"**:
  settle the message before designing, the way you outline before writing
  (Rougier, Droettboom & Bourne, PLOS Comput Biol 10(9):e1003833,
  https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833).
- **If you fail to name the claim, the figure is decoration.** Delete it, or
  demote it to one sentence of text. A paper pays for a figure in page area, so
  each one earns its rent by removing a paragraph.
- **One figure, one job.** A second claim earns a second panel, not a second axis
  crammed onto the first. Panels labeled (a), (b), (c) are cheap; overloaded axes
  are not.
- **Write the claim down and keep it.** It becomes the caption's closing sentence
  later (see `caption-writing`), so drafting it now costs nothing twice.
- **Rank the figure before drawing.** A flagship figure carries the paper's
  headline result and earns width, panels, and a long caption. A workhorse figure
  documents a mechanism and earns a compact canvas.
- **Rule 9, message trumps beauty**: readability of the message is the point, and
  beauty is optional (same source as above).
- *Toy:* TileSort's claim is "rejecting low-confidence tiles raises bin purity at
  a small throughput cost." One claim, two quantities, one figure.
---

## Part 2: Pick the form

### The chart-type heuristic

Match the mark to the question, not to habit.

| The question | The form | Watch for |
|---|---|---|
| **Comparison** across a few categories | Horizontal bars or a dot plot, sorted by value | Sort by value, never alphabetically; bars start at zero |
| **Distribution** of one variable | Histogram, ECDF, box or violin; strip plot with raw points when n is small | Show the raw points whenever n is under about 30 |
| **Relationship** between two variables | Scatter; a line only when x is ordered | Do not connect unordered categories with a line |
| **Trend** over a controlled variable | Line with an error band over seeds | Say in the caption what the band is (SD, SE, or range) |
| **Composition** of a whole | Stacked bar, but only when the total is meaningful | Never a pie chart |
| **Flow and architecture** | A diagram: boxes, arrows, one worked instance | Go to the Figma track, Part 3 |
| **The same chart across conditions** | Small multiples on shared axes | Shared axis limits, one legend for the grid |

Rule 7 of the Ten Simple Rules rejects pie charts, 3D charts, and auto-scaled
axes that distort perception, and asks for full value ranges and labels
(https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833).

### When a table beats a plot

- **Under about twenty numbers, use a table.** Tufte: "Tables usually outperform
  graphics in reporting on small data sets of 20 numbers or less" (*The Visual
  Display of Quantitative Information*, 1983).
- **Use a table when readers will quote the number.** Benchmark scoreboards get
  cited digit by digit, and a bar chart forces the reader to estimate.
- **Use a table when the rows have different units.** A plot needs one shared
  scale; a table needs none.
- **Use a plot when the shape is the finding**: a crossover, a plateau, a
  heavy tail, a scaling slope. Shape survives a glance; a table does not.
- **Never ship both for the same numbers.** Pick one and reference it.

### Tufte discipline, applied to ML plots

- **Raise the data-ink ratio by subtraction.** Delete the top and right spines,
  the legend box, the background fill, the heavy grid, the redundant tick labels.
  Tufte defines data-ink as the non-erasable core of a graphic and chartjunk as
  ink that tells the viewer nothing new (*The Visual Display of Quantitative
  Information*, 1983).
- **Keep a faint horizontal grid only when readers must compare values across a
  wide gap.** Set it behind the data at low weight.
- **Prefer small multiples to a five-series spaghetti plot.** Five lines in one
  panel is five chances to misread; five small panels is one shared reading.
- **Rule 8, avoid chartjunk**, and **Rule 5, do not trust the defaults**: default
  settings "are good enough for any plot but they are best for none" (Rougier et
  al., URL above).
---

## Part 3: The system-diagram track (authoring in Figma)

Architecture and pipeline figures are drawn, not plotted. A vector design tool
beats TikZ for iteration speed and beats slides for precision. The discipline
below is what stops a hand-placed diagram from looking hand-placed.

### 3.1 Size the frame to the column, first

Figma's canvas runs at 72 pixels per inch, so one Figma pixel maps to one
PostScript point. A US Letter page is therefore 612 by 792 px (Figma for Print
FAQ, https://johannesippen.com/2025/figma-print-faq/). Frame width in pixels is
**inches times 72**:

| Venue | Layout | Text block | Figure width | Figma frame width |
|---|---|---|---|---|
| NeurIPS | single column | 5.5 in wide, 9 in tall | 5.5 in | **396 px** |
| ICLR | single column | 5.5 in wide, 9 in tall | 5.5 in | **396 px** |
| ICML | two column | 6.75 in wide, 9.0 in tall, 0.25 in gutter | 3.25 in per column | **234 px** |
| ICML, spanning figure | two column | as above | 6.75 in | **486 px** |

Sources for the numbers. The NeurIPS style file sets `textheight=9in,
textwidth=5.5in`
(https://media.neurips.cc/Conferences/NeurIPS2022/Styles/neurips_2022.sty). The
ICLR 2025 instructions state "The text must be confined within a rectangle 5.5
inches (33 picas) wide and 9 inches (54 picas) long"
(https://arxiv.org/html/2409.06957v1). The ICML 2025 instructions state the text
is "formatted in two columns, with an overall width of 6.75 inches, height of 9.0
inches, and 0.25 inches between the columns"
(https://arxiv.org/html/2502.04757v1). That leaves (6.75 - 0.25) / 2 = 3.25 in
per column. Check the current year's style file before trusting any of these.

Set the frame height to what the content needs. Keep a single-column figure under
about a third of the 9 in text height so it never eats a page alone.

### 3.2 Build on an 8 px grid

- **Set the layout grid to 8 px and snap everything to it.** Every gap, padding
  value, and box dimension becomes a multiple of 8, with 4 px allowed for tight
  optical corrections. Figma's own design-system lesson builds spacing and text
  styles around this grid (https://help.figma.com/hc/en-us/articles/14548865734679).
- **Why 8 and not 10:** 8 divides cleanly at half and quarter steps, so nested
  padding stays on grid. On a 234 px frame, 8 px of padding reads as roughly
  3 percent of the width, which is a visible but modest margin.
- **One gutter value for the whole figure.** Pick 16 px or 24 px between blocks
  and reuse it. Two gutter values in one diagram read as an accident.

### 3.3 Components, auto layout, and styles

- **Make every repeated block a component.** A pipeline with four module boxes
  has one master box component and four instances, so a change to the corner
  radius or the padding propagates everywhere at once.
- **Use auto layout for anything with padding or a stack.** Auto layout defines
  the space between layers and the vertical and horizontal padding, and holds the
  spacing as the content changes
  (https://help.figma.com/hc/en-us/articles/14548865734679). Set the frame to a
  fixed width so auto layout grows the height only.
- **Bind color styles and text styles, never raw hex or raw font sizes.** Define
  `fig/blue`, `fig/orange`, `fig/gray-200`, `fig/label`, `fig/annotation` once,
  in a shared library, and every figure in the paper inherits them. A palette
  change then costs one edit rather than eleven files.
- **Name every layer for what it is.** `scanner-box`, `arrow-scanner-to-sorter`,
  `label-reject-rate`. Layer names become SVG `id` attributes when the export
  option "Include 'id' attribute" is on
  (https://help.figma.com/hc/en-us/articles/13402894554519-Export-formats-and-settings),
  so good names survive into the file and make later edits fast.
- **One page per paper, one frame per figure, named `fig1-pipeline`,
  `fig2-ablation`.** The filename you export becomes the filename LaTeX includes.

### 3.4 Alignment and formatting discipline

The details below are what separate a diagram that reads as designed from one
that reads as assembled.

- **One arrowhead style everywhere.** Pick one shape, one size, one stroke
  weight, and use it for every arrow in every figure of the paper. Mixed
  arrowheads read as two authors.
- **One corner radius everywhere.** Pick 4 px or 6 px for boxes and never vary
  it. Radius variation implies a semantic difference that does not exist.
- **One stroke weight per role.** For example: 1 px for box outlines, 1.5 px for
  data-flow arrows, 0.75 px for annotation leaders. Three roles maximum, and
  nothing below 0.75 px so every line clears the 0.5 pt reproduction floor.
- **Align edges, then align optically.** Snap boxes to shared x or y edges with
  Figma's align tools, then correct by eye. A shape's visual center often differs
  from its bounding box, which happens with triangles, arrowheads, and
  parentheses. Optical alignment beats numeric alignment when they disagree.
- **Consistent gutters beat centered composition.** Equal spacing between
  siblings reads as order; a centered but unevenly spaced row reads as drift.
- **Label placement rules, fixed once:** box labels centered inside the box;
  edge labels above a horizontal arrow and to the right of a vertical arrow;
  units in the axis or legend label, never floating; a legend inside the frame
  only when it fits without overlapping a mark.
- **Text stays live, and stays on one family.** Use the paper's font family for
  every label so the figure does not announce itself as foreign. A serif paper
  takes serif labels.
- **Kill decoration.** No drop shadows, no gradients, no background fills, no 3D
  boxes. Shadows and blurs also force Figma's PDF exporter to rasterize the
  blurred region (https://www.figma.com/blog/our-path-to-creating-the-highest-quality-pdf-exporter/),
  which puts pixels into an otherwise vector figure.

### 3.5 Exporting for LaTeX without breaking anything

- **Export the frame as PDF at 1x.** Figma supports SVG and PDF export at 1x
  only, and the scale setting does not apply to them
  (https://help.figma.com/hc/en-us/articles/13402894554519-Export-formats-and-settings).
  Because the frame was built at the column width, 1x is exactly what you want.
- **The stroke-weight trap.** Strokes are specified in pixels, so a 1 px stroke
  exports as a 1 pt line. Design a 468 px frame and include it at 3.25 in, and
  every stroke halves to 0.5 pt while every label halves in size. Design at final
  width, export 1x, include at 1.0, and no scaling ever touches the file.
- **ICML sets the floor: "Lines should be dark and at least 0.5 points thick for
  purposes of reproduction"** (https://arxiv.org/html/2502.04757v1). Keep the
  thinnest stroke at 0.75 px or above so it clears the floor with margin.
- **Prefer center-aligned strokes.** SVG supports center strokes only, so Figma's
  "Simplify stroke" option converts inside and outside strokes on export
  (https://help.figma.com/hc/en-us/articles/13402894554519-Export-formats-and-settings).
  Center strokes avoid the conversion entirely.
- **Turn on "Clip content" for the frame** so nothing bleeds past the artboard,
  and confirm no element sits outside the frame bounds before export.
- **Avoid the Plus darker and Plus lighter blend modes**, which PDF export does
  not support (same Figma help page).
- **If you export SVG instead of PDF**, note that text is exported as glyph
  outlines by default ("Outline text"), which guarantees the shapes but kills
  text selection and search. Convert with `rsvg-convert -f pdf` or `inkscape
  --export-type=pdf` before including in LaTeX, or use the `svg` package.
- **Verify the exported file** with the Part 7 checklist: `pdfinfo` must report
  the page width you designed, and `pdffonts` must show every font embedded.
---

## Part 4: The plot track (matplotlib)

Data figures come from code, so the style lives in code and the figure is
reproducible from the results file.

### 4.1 The defaults are wrong, on purpose

- matplotlib ships `figure.figsize: 6.4, 4.8` inches
  (https://raw.githubusercontent.com/matplotlib/matplotlib/main/lib/matplotlib/mpl-data/matplotlibrc).
  Include that 6.4 in canvas in a 3.25 in ICML column and LaTeX scales it by
  3.25 / 6.4 = 0.51, so 10 pt tick labels print at about 5 pt. Illegible, and a
  routine reason reviewers flag a figure.
- matplotlib ships `pdf.fonttype: 3` and `ps.fonttype: 3`, both documented as
  "Output Type 3 (Type3) or Type 42 (TrueType)" (same file). arXiv asks that
  "outline (TrueType/Type1) rather than bitmap (Type3) fonts are used"
  (https://info.arxiv.org/help/submit_pdf.html), so 3 must become 42.
- Rule 5 of the Ten Simple Rules says the same thing in general: do not trust the
  defaults (https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833).

### 4.2 The publication rcParams block

Put this at the top of the plotting module, once, and import it everywhere.

```python
import matplotlib as mpl

COLUMN_IN = 3.25          # ICML column. Use 5.5 for NeurIPS and ICLR.
CAPTION_PT = 9            # ICML caption size; figure text never goes below it.

OKABE_ITO = ["#0072B2", "#D55E00", "#009E73", "#CC79A7",
             "#E69F00", "#56B4E9", "#F0E442", "#000000"]

mpl.rcParams.update({
    # Geometry: build at the final printed width so nothing is rescaled.
    "figure.figsize":   (COLUMN_IN, COLUMN_IN * 0.62),
    "figure.dpi":       200,        # screen preview only
    "savefig.dpi":      400,        # matters only for embedded raster
    "savefig.bbox":     "standard", # keep the page exactly figsize
    "savefig.format":   "pdf",
    "figure.constrained_layout.use": True,   # fit labels without cropping

    # Fonts: embed TrueType, match the paper's serif family.
    "pdf.fonttype":     42,         # default is 3
    "ps.fonttype":      42,
    "font.family":      "serif",
    "font.serif":       ["Times New Roman", "Nimbus Roman", "DejaVu Serif"],
    "mathtext.fontset": "stix",     # Times-compatible math

    # Type sizes: nothing below the caption size.
    "font.size":        CAPTION_PT,
    "axes.titlesize":   CAPTION_PT,
    "axes.labelsize":   CAPTION_PT,
    "xtick.labelsize":  CAPTION_PT,
    "ytick.labelsize":  CAPTION_PT,
    "legend.fontsize":  CAPTION_PT,

    # Strokes: ICML floor is 0.5 pt, so stay above it.
    "axes.linewidth":       0.6,
    "lines.linewidth":      1.2,
    "lines.markersize":     3.5,
    "xtick.major.width":    0.6,
    "ytick.major.width":    0.6,
    "grid.linewidth":       0.4,

    # Ink: delete what encodes nothing.
    "axes.spines.top":      False,
    "axes.spines.right":    False,
    "legend.frameon":       False,
    "axes.grid":            False,
    "axes.prop_cycle":      mpl.cycler(color=OKABE_ITO),
})
```

Notes on the choices:

- **`figure.figsize` is the whole ballgame.** Set the width to the column width
  in inches and let the height follow from the content. A ratio near 0.62 (the
  golden ratio) suits a single-panel line plot; a bar chart with long category
  names goes taller.
- **Keep `savefig.bbox` at `"standard"` and let constrained layout do the
  fitting.** `bbox="tight"` crops the saved page to the drawn content, so the
  file comes out narrower than `figsize` and `width=\columnwidth` then scales it
  back up by a percent or two. Constrained layout instead shrinks the axes to fit
  the labels inside the declared size, so the exported width stays exact.
- **If 9 pt labels collide, the figure holds too much.** Drop a series, shorten
  the tick labels, or promote to a spanning figure. Never shrink the type.
- **`text.usetex: True` or the PGF backend** makes the figure's math and text
  identical to the paper's, at the cost of a TeX run per figure. Turn it on when
  math appears inside the figure. Otherwise leave it off: the serif family above
  is close enough, and the build stays fast.

### 4.3 Plot hygiene

- **Label both axes with the quantity and the unit**: "Belt speed (tiles/s)",
  not "speed". ICML asks authors to "give a name for each axis and include a
  legend" (https://arxiv.org/html/2502.04757v1), and a unitless axis leaves the
  reader guessing at the scale.
- **Show uncertainty.** Multiple seeds get a band or error bars, and the caption
  states what the band is. A single-seed curve claims a precision it lacks.
- **Start bar axes at zero.** Truncated bar axes exaggerate differences, which
  Rule 7 calls out as misleading the reader (Rougier et al., URL above). A
  truncated line axis is legal when the caption states the range.
- **Sort categories by value**, not alphabetically, so the eye reads the ranking
  without decoding the labels.
- **Direct-label the series when there are three or fewer**, placing the name at
  the end of its line. Okabe and Ito recommend labels placed inside the drawing
  and connected by thin lines, so the reader stops matching a distant key
  (https://jfly.uni-koeln.de/color/).
- **Never a second y-axis with a different unit.** Split into two stacked panels
  sharing the x axis.
- **Save the script beside the figure** and regenerate from the results file, so
  no number in the figure is typed by hand.
---

## Part 5: Typography and size

- **The hard rule: figure text is never smaller than the caption text.** ICML's
  accessibility guidance states it exactly: "The font size in figures should be
  no smaller than the font size of the caption of the figure"
  (https://icml.cc/Conferences/2023/AccessiblePapersAndTalks).
- **What that means numerically.** ICML sets captions in 9-point type and body
  text at 10 pt on 11 pt leading (https://arxiv.org/html/2502.04757v1). NeurIPS
  and ICLR also use 10 pt on 11 pt, with `\small` at 9 pt
  (https://media.neurips.cc/Conferences/NeurIPS2022/Styles/neurips_2022.sty,
  https://arxiv.org/html/2409.06957v1). So **9 pt is the floor for ML venue
  figure text**, and 9 to 10 pt is the working range.
- **For contrast, print journals allow smaller.** Nature's artwork guide asks for
  5 pt minimum and 7 pt maximum at their 90 mm and 180 mm widths
  (https://www.nature.com/documents/nature-final-artwork.pdf). Those numbers
  belong to a different production pipeline; do not import them into an ML paper.
- **Match the paper's typeface.** NeurIPS and ICLR name Times New Roman as the
  preferred face (https://arxiv.org/html/2409.06957v1), so figure labels go
  serif. Nature asks for sans-serif labels instead
  (https://www.nature.com/documents/nature-final-artwork.pdf). The rule is match
  your venue, not pick a favorite.
- **One family and at most two sizes per figure.** Labels at 9 pt, panel letters
  at 9 pt bold. A third size is noise.
- **Figure text carries data only.** Axis quantities, units, category names, and
  panel letters. Model names, method qualifiers, hedges, and claims belong in the
  caption, where prose is allowed and the reader expects argument. A canvas
  crowded with qualifiers reads as a slide, not a figure.
- **Expand or drop abbreviations.** If an axis label needs an abbreviation to
  fit, the abbreviation is decoded in the caption on first use.
- **Sentence case for labels, and no terminal period.** Write `Bin purity (%)`.
  Do not write `Bin Purity (%)` in title case, and do not end an axis label with
  a period.
- **Check at 100 percent, on paper.** Print the page and read it at arm's length.
  A figure that survives a monochrome office printer survives anything.
---

## Part 6: Color

### The default palette

Use the Okabe-Ito eight-color qualitative set, designed so that the colors stay
unambiguous to viewers with and without color vision deficiency (Okabe & Ito,
Color Universal Design, https://jfly.uni-koeln.de/color/):

| Name | Hex |
|---|---|
| Blue | `#0072B2` |
| Vermilion | `#D55E00` |
| Bluish green | `#009E73` |
| Reddish purple | `#CC79A7` |
| Orange | `#E69F00` |
| Sky blue | `#56B4E9` |
| Yellow | `#F0E442` |
| Black | `#000000` |

Order matters: the first three are the most separable, so a three-series plot
takes blue, vermilion, and bluish green. Yellow is weak on white, so it goes last
or gets a dark outline. For map-style data, ColorBrewer offers sequential,
diverging, and qualitative schemes with an explicit colorblind-safe filter
(Brewer & Harrower, https://colorbrewer2.org/).

### Matching the colormap to the data type

Rule 6 of the Ten Simple Rules sets the mapping
(https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833):

- **Sequential** (low to high): one hue varying in lightness. Use viridis, which
  matplotlib adopted as its default replacement for jet.
- **Diverging** (deviation from a midpoint): two hues meeting at a neutral
  center, with the center pinned to the meaningful zero.
- **Qualitative** (unordered categories): the Okabe-Ito set above.

### Why jet and rainbow are rejected

- Rule 6 says to avoid jet and rainbow "as much as possible" absent an explicit
  reason (Rougier et al., URL above).
- Borland & Taylor show three failures of the rainbow map: it confuses through
  its lack of perceptual ordering, obscures data through uncontrolled luminance
  variation, and misleads by introducing gradients the data does not contain
  ("Rainbow Color Map (Still) Considered Harmful", IEEE CG&A 27(2):14-17, 2007,
  https://ieeexplore.ieee.org/document/4118486/).
- Crameri, Shephard & Heron document that colormaps distorting data through
  uneven gradients, or unreadable under color vision deficiency, remain common,
  and name rainbow-like and red-green maps specifically ("The misuse of colour in
  science communication", Nature Communications 11:5444, 2020,
  https://www.nature.com/articles/s41467-020-19160-7).
- Practical consequence: a red-green pairing is the one both sources name as
  unreadable, and it stays common in ML papers. Use blue and vermilion.

### Redundant encoding, the non-negotiable

Okabe and Ito state the principle directly: use "not only different colors but
also a combination of different shapes, positions, line types and coloring
patterns" (https://jfly.uni-koeln.de/color/). ICML repeats it: "Do not rely on
color to convey information" (https://icml.cc/Conferences/2023/AccessiblePapersAndTalks).

So every series gets three encodings at once:

| Series | Color | Line style | Marker |
|---|---|---|---|
| 1 | `#0072B2` blue | solid | circle |
| 2 | `#D55E00` vermilion | dashed | square |
| 3 | `#009E73` bluish green | dotted | triangle |

For bars and heatmaps, the redundant channel is a hatch pattern or a printed
value inside the cell.

### The grayscale check

- ICLR states the standard: "it is best for the figure captions and the paper
  body to make sense if the paper is printed either in black/white or in color"
  (https://arxiv.org/html/2409.06957v1).
- Convert and look, do not imagine:
  `gs -sDEVICE=pdfwrite -sColorConversionStrategy=Gray -dProcessColorModel=/DeviceGray -dNOPAUSE -dBATCH -o gray.pdf fig.pdf`
- If two series merge in gray, the line styles were doing no work. Fix the
  encoding, not the color.
- Simulate color vision deficiency with a checker such as Coblis
  (https://www.color-blindness.com/coblis-color-blindness-simulator/) for the
  deuteranope and protanope cases.
- **Text stays off gray backgrounds.** ICML: "text should not appear on a gray
  background" (https://arxiv.org/html/2502.04757v1).
---

## Part 7: The mechanical checklist, run before every submission

Each box is a check-and-fix, not an opinion. Run it on the compiled paper PDF,
not on the figure in isolation.

### Format and file
- [ ] **Vector for anything drawn.** ICML asks for vector eps or pdf for line and
  bar plots, lossless png for sharp-lined raster, jpeg for photographs
  (https://arxiv.org/html/2502.04757v1).
- [ ] **`pdffonts fig.pdf`**: every row shows `yes` in the `emb` column, and no
  row's type is `Type 3`. arXiv asks for outline rather than bitmap fonts
  (https://info.arxiv.org/help/submit_pdf.html).
- [ ] **`pdfinfo fig.pdf`**: the page size in points equals the design width
  times 72 (3.25 in reads as 234 pts, 5.5 in as 396 pts). A smaller number means
  a tight bounding box cropped the page and LaTeX is scaling it back up.
- [ ] **No rescaling in the include.** `\includegraphics[width=\columnwidth]` on
  a figure already built at column width scales by 1.0. Search the source for
  `scale=`, `height=`, and `width=0.` factors and fix each at the source figure.
- [ ] **`width=\columnwidth` inside a two-column `figure`**, `width=\textwidth`
  only inside `figure*`. Mixing them silently rescales.
- [ ] **Embedded raster is 300 dpi or better** at final printed size.

### Legibility
- [ ] **No text in the figure is smaller than the caption text**
  (https://icml.cc/Conferences/2023/AccessiblePapersAndTalks).
- [ ] **Every line is at least 0.5 pt after any scaling**
  (https://arxiv.org/html/2502.04757v1).
- [ ] **Printed the page on paper and read it at arm's length.**
- [ ] **No text sits on a gray background** (same ICML source).

### Content
- [ ] **Every axis names its quantity and its unit.**
- [ ] **Every distinct component is labeled**, and a graph names each axis and
  includes a legend (https://arxiv.org/html/2502.04757v1).
- [ ] **Every mark on the canvas is decoded exactly once**, in the legend or the
  caption, never in both.
- [ ] **The legend does not repeat the caption**, and the caption does not
  re-list the legend entries.
- [ ] **Error bars or bands are present** wherever a quantity varies across
  seeds, and the caption says what they represent.
- [ ] **Axes are not truncated** without the caption saying so; bar axes start at
  zero.
- [ ] **No chartjunk**: no 3D, no gradients, no drop shadows, no box frame, no
  heavy grid.
- [ ] **Figure text carries data only**: no model names, no qualifiers, no
  claims on the canvas.

### Accessibility
- [ ] **Color is never the only encoding**; every series also has a line style,
  marker, or hatch (https://jfly.uni-koeln.de/color/).
- [ ] **Grayscale conversion is still readable**
  (https://arxiv.org/html/2409.06957v1).
- [ ] **No jet or rainbow colormap** (https://ieeexplore.ieee.org/document/4118486/).
- [ ] **Alt text is written** for the camera-ready, in plain language, describing
  content and function rather than repeating the caption
  (https://www.sigaccess.org/welcome-to-sigaccess/resources/describing-figures/).

### Placement
- [ ] **The figure sits at the top of a page or column**, above its first
  reference where possible.
- [ ] **The caption is not separated from the figure across a page break**
  (https://arxiv.org/html/2409.06957v1).
- [ ] **Every figure is referenced in the body by number**, and the reference
  makes a point rather than saying "see Figure 3".
---

## Part 8: A worked example, claim to shipped PDF

TileSort ships two figures. Here is the second one, end to end.

**1. Name the job.** The claim: "rejecting low-confidence tiles raises bin purity
at a small throughput cost." Two quantities, one controlled variable, three
system variants.

**2. Pick the form.** Belt speed is an ordered controlled variable, so the
question is a trend, and the form is a line plot with an uncertainty band over
five seeds. Two panels share the x axis: purity on the left, throughput on the
right. A table would hide the crossover, which is the finding.

**3. Size the canvas.** The paper targets ICML, so the column is 3.25 in wide.
Two panels side by side would leave each about 1.6 in, too narrow for 9 pt
labels, so the figure spans both columns in a `figure*` at 6.75 in by 2.1 in.

**4. Build it.** The plotting script imports the Part 4.2 rcParams block, sets
`figure.figsize` to `(6.75, 2.1)`, reads `results/purity_by_speed.csv`, and draws
three series per panel:

| Variant | Color | Line style | Marker |
|---|---|---|---|
| No reject | `#0072B2` | solid | circle |
| Fixed threshold | `#D55E00` | dashed | square |
| Learned threshold | `#009E73` | dotted | triangle |

Each series is a mean over five seeds with a shaded band at one standard
deviation. Axes: "Belt speed (tiles/s)" on x, "Bin purity (%)" on the left panel,
"Throughput (tiles/min)" on the right. Top and right spines off, legend frame
off, three series direct-labeled at the line ends so no legend is needed.

**5. Check the type.** Every label is 9 pt, equal to the ICML caption size. The
right panel's tick labels collided at first, so the script drops from six ticks
to four rather than shrinking the type.

**6. Check the color.** Convert to gray with Ghostscript: the three lines stay
separable because solid, dashed, and dotted do the work. Simulate deuteranopia:
blue, vermilion, and bluish green stay distinct.

**7. Export and verify.**
```
python figs/purity_vs_speed.py           # writes figs/purity_vs_speed.pdf
pdfinfo  figs/purity_vs_speed.pdf        # Page size: 486 x 151 pts  -> 6.75 in
pdffonts figs/purity_vs_speed.pdf        # emb=yes on every row, no Type 3
```

**8. Place it.**
```latex
\begin{figure*}[t]
  \centering
  \includegraphics[width=\textwidth]{figs/purity_vs_speed.pdf}
  \caption{Name the exhibit. Decode every mark. Land the claim.}
  \label{fig:purity-vs-speed}
\end{figure*}
```
`\textwidth` is 6.75 in and the PDF is 6.75 in, so the scale factor is 1.0 and
the 9 pt labels print at 9 pt.

**9. Write the caption** with the `caption-writing` skill: name the exhibit,
decode every mark, land the claim with its numbers. Then read the compiled page
and confirm nothing reflowed.

**The companion diagram, for contrast.** TileSort's Figure 1 is the pipeline, so
it goes to the Figma track. One frame, 234 px wide, on an 8 px grid with 16 px
gutters. One box component, instanced three times for the scanner, the sorter,
and the reject chute. One arrowhead style, one 4 px corner radius, labels
centered in the boxes and set in the paper's serif face at 9 pt. Color styles
`fig/blue` and `fig/gray-200` come from the shared library, and layers are named
`scanner-box` and `arrow-scanner-to-sorter`. Export as PDF at 1x, verify the page
reads 234 pts wide, include at `width=\columnwidth`.
---

## Part 9: The figure and its caption are one exhibit

A figure is never audited alone. The figure, its caption, and the table it
corresponds to form one exhibit, and they are checked together.

- **The caption carries the claim; the canvas carries the data.** Rule 4 of the
  Ten Simple Rules: captions are not optional, they explain how to read the
  figure and supply the context
  (https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833).
- **One vocabulary across the exhibit.** Legend entries, axis names, and bar
  labels use the caption's exact terms. When the caption points at a table, the
  labels match that table's row names word for word. A mismatch means
  regenerating the figure, not rewording the caption.
- **Decode every mark exactly once**, in the legend or the caption, never both.
  A legend that repeats the caption wastes the canvas; a caption that re-lists
  the legend wastes the reader.
- **Hand off now.** Write the caption with the `caption-writing` skill in this
  repo: name the exhibit with a verbless noun phrase, decode the reading keys,
  land the claim as the closer. Then run `sentence-audit` over the caption and
  any figure-adjacent body text.
---

## Sources

Venue style and author instructions:
- NeurIPS 2022 style file (text block 5.5 in by 9 in, 10 pt on 11 pt, `\small`
  at 9 pt): https://media.neurips.cc/Conferences/NeurIPS2022/Styles/neurips_2022.sty
- ICLR 2025 formatting instructions (5.5 in by 9 in rectangle, 10 pt on 11 pt,
  Times New Roman, black-and-white legibility, caption placement):
  https://arxiv.org/html/2409.06957v1
- ICML 2025 submission and formatting instructions (6.75 in by 9.0 in, 0.25 in
  gutter, 9-point captions, 0.5 pt minimum line thickness, label all components,
  vector preferred, no text on gray): https://arxiv.org/html/2502.04757v1
- ICML accessible papers guidance (figure text no smaller than caption text, do
  not rely on color alone, high contrast):
  https://icml.cc/Conferences/2023/AccessiblePapersAndTalks
- arXiv PDF submission guidance (outline rather than bitmap Type 3 fonts, all
  fonts embedded): https://info.arxiv.org/help/submit_pdf.html

Design principles:
- Rougier, Droettboom & Bourne, "Ten Simple Rules for Better Figures", PLOS
  Computational Biology 10(9):e1003833, 2014:
  https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833
- Tufte, *The Visual Display of Quantitative Information*, 1983 (data-ink ratio,
  chartjunk, small multiples, tables for 20 numbers or fewer).

Color:
- Okabe & Ito, Color Universal Design (the eight-color palette, redundant
  encoding, direct labeling): https://jfly.uni-koeln.de/color/
- Brewer & Harrower, ColorBrewer (sequential, diverging, qualitative schemes with
  a colorblind-safe filter): https://colorbrewer2.org/
- Borland & Taylor, "Rainbow Color Map (Still) Considered Harmful", IEEE Computer
  Graphics and Applications 27(2):14-17, 2007:
  https://ieeexplore.ieee.org/document/4118486/
- Crameri, Shephard & Heron, "The misuse of colour in science communication",
  Nature Communications 11:5444, 2020:
  https://www.nature.com/articles/s41467-020-19160-7

Tools:
- matplotlib default rcParams (`figure.figsize: 6.4, 4.8`; `pdf.fonttype: 3`):
  https://raw.githubusercontent.com/matplotlib/matplotlib/main/lib/matplotlib/mpl-data/matplotlibrc
- Figma export formats and settings (SVG and PDF at 1x only, outline text,
  simplify stroke, id attribute, unsupported blend modes):
  https://help.figma.com/hc/en-us/articles/13402894554519-Export-formats-and-settings
- Figma design-system lesson (auto layout spacing and padding, shared styles):
  https://help.figma.com/hc/en-us/articles/14548865734679
- Figma PDF exporter engineering note (shadows and blurs rasterize a region):
  https://www.figma.com/blog/our-path-to-creating-the-highest-quality-pdf-exporter/
- Figma for print FAQ (72 pixels per inch, US Letter is 612 by 792 px):
  https://johannesippen.com/2025/figma-print-faq/

Accessibility:
- SIGACCESS guide to describing figures (alt text that gives content and
  function, not a repeat of the caption):
  https://www.sigaccess.org/welcome-to-sigaccess/resources/describing-figures/
- Nature final artwork guide (5 pt minimum, 7 pt maximum, sans-serif labels, at
  90 mm and 180 mm widths; a print-journal regime, not an ML venue one):
  https://www.nature.com/documents/nature-final-artwork.pdf
---

**Semicolon rule (addendum).** A semicolon is earned only by a true antithesis or
a tightly parallel pair; everything else takes a period. Budget about two per
part. After any editing pass, grep `;`: each survivor names its antithesis or
becomes a period.
