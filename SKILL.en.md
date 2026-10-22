---
name: kai-writing
description: Draft or revise introductions, results, and discussions for Chinese or English academic papers in quantitative finance, statistics, and machine learning using supplied research material. Select rules by target language and section, preserving the study's facts and evidence.
---

# kai-writing · Academic writing in Chinese and English

## Usage and mode selection

Select a mode using the user's target language and section, then apply the shared guidelines, applicable conditional paragraphs, and the selected section module. If no language is specified, follow the main language of the source material.

“Chinese only” applies to the three Chinese section modes; “English only” applies to the three English modes; “Chinese Discussion only” applies only to Chinese discussion/conclusion text. In the shared guidelines, a scope label applies only to the single paragraph immediately after it. Unlabeled paragraphs are shared rules. A section-module heading, by contrast, governs the entire module beneath it. Do not apply mutually exclusive conditions together. Examples for other languages or sections do not guide the current manuscript. For a request covering several sections or both Chinese and English drafts, select a mode separately for each part.

At the start of writing, repeat the selected mode's deployment-package, standing-instruction, and section-module versions. Versions belonging to inactive modes do not constitute conflicts.

| Mode | Target manuscript | Standing-instruction version |
|---|---|---|
| CN-INTRO | Chinese Introduction | core-pilot-v0.1-experimental-v7-ad12-s1 |
| CN-RESULTS | Chinese Results | core-pilot-v0.1-experimental-v7-ad12-s1 |
| CN-DISCUSSION | Chinese Discussion or Conclusion | core-pilot-v0.1-experimental-v7-claim-state-dev1-ad12-s1 |
| EN-INTRO | English Introduction | en-core-pilot-v0.1-experimental-v1-ad12-s1 |
| EN-RESULTS | English Results | en-core-pilot-v0.1-experimental-v1-ad12-s1 |
| EN-DISCUSSION | English Discussion or Conclusion | en-core-pilot-v0.1-experimental-v1-ad12-s1 |

Provide research notes, results tables, or a rough draft, and specify the audience and length. Complex inputs may be divided into “research content that must be included / preceding background for understanding / editing instructions.” Do not invent facts to fill a template. References below to “this file and one section module” mean the shared guidelines, applicable conditional paragraphs, and selected module within this file; they do not require another file.

## Shared guidelines and language-specific execution

### Task and audience

Write Chinese or English academic prose for busy, exacting peers familiar with the field. Follow the user's language, section, journal, and style requirements; if the language is unspecified, follow the main language of the source material. Present the research subject, methods, evidence, reasoning, and conditions accurately. Do not praise the results or announce their significance on the reader's behalf. Establish each paragraph's subject, question, or claim promptly, and make every sentence advance the information.

The deployment package for each writing task consists of this file and one section module. Before writing, reproduce the standing-instruction and section-module versions exactly outside the manuscript code block. Stop if either version is missing, conflicting, or cannot be reproduced; do not substitute another version from memory. The current deployment package is the sole applicable specification.

### Claims supported by the material

Use only the material supplied for the current task. Facts, numbers, citations, method details, comparison groups, explanations, and conclusions must all be traceable to that material. Do not fill gaps from general knowledge, transfer topics, variables, numbers, quotations, or conclusions from a section module into the manuscript, or add material merely to match an example's information density. Background, term definitions, figure legends, and axis descriptions help interpret the material; they are not a checklist of content that must appear in the manuscript. Include only what readers need to understand the current subject, comparison, or claim. Treat unlabeled fragments by their purpose too: retain research claims and their grounds, without repeating editing instructions or figure-layout notes. This does not authorize omitting units, denominators, groups, metric definitions, necessary legend mappings, or content the user explicitly requires. If a gap does not prevent completing the task, omit the affected content. If it does, identify the specific missing material outside the manuscript code block instead of filling it with placeholders or vague assertions.

Preserve the original strength and scope of the evidence. Do not turn correlation into causation, predictive performance into evidence of a mechanism, in-sample findings into unconditional out-of-sample claims, a local sample into a population, or statistical significance into automatic practical importance. Retain the research subject, temporal and spatial scope, sample definition, units, signs, denominator, reference group, uncertainty, and other qualifications. Preserve whether the material describes something achieved, possible, required, or intended; this also applies to method properties, findings from prior work, and adverse consequences. Keep a possible explanation hypothetical. A nonsignificant result is not evidence of no effect, robustness checks do not eliminate every bias, and explanatory metrics do not establish causal contributions.

Distinguish findings of the present study, conclusions from existing literature, and the authors' explanations. Retain only supplied sources and the claims they support. Do not invent authors, years, pages, links, or placeholder citations, or move a citation to a stronger claim. When revising a literature review, preserve the complete research object specified by the heading or introductory wording. A model that uses a method is not the method itself, and changing the grammatical subject to the authors does not justify crediting them with introducing or inventing it. Place separate citations near the distinct claims they support. Preserve table, figure, equation, variable, and appendix identifiers; do not cite objects absent from the material. Do not combine numbers from different sources into a new statistic not supplied by the material. Calculate only when the inputs, formula, and definitions are complete.

After drafting, trace each sentence back to its support. Delete unsupported evaluations or extrapolations, or revise them into supported claims using subjects, conditions, and evidence already supplied. Do not replace an exaggerated conclusion with a newly invented negative conclusion. The absence of a test from the supplied material does not mean the study did not conduct it. More natural wording must not change facts, omit necessary conditions, or strengthen, weaken, or narrow conclusions. Preserve research information rather than the form of the original sentence. Repeated expressions of the same meaning and unnecessary equivalents in another language do not count as additional research information.

### Whole manuscripts and paragraphs

**Chinese only:**

The user's explicit requirements for the final manuscript's paragraph count, order, or paragraph functions override the default paragraph organization in this section. The number of paragraphs in source material, an original text, or a quotation is not itself a requirement for the final manuscript. “One paragraph” must not be interpreted as one paragraph per task. If the user gives conflicting final paragraph counts, identify the conflict outside the manuscript code block and stop. If only order or paragraph functions are specified, follow them first, then determine the number of paragraphs from the information structure. Apply the defaults below in full only when count, order, and paragraph functions are all unspecified.

Write ordinary narrative manuscript text in complete paragraphs, without bullet lists or bold emphasis used for rhetoric. Do not default to three parallel items or add a separate paragraph merely to appear comprehensive. Journal-required structured abstracts, algorithms, hypotheses, theorems, figure and table notes, mathematical boldface, and formats explicitly requested by the user are exempt. Do not add sweeping historical background, promotional openings, section road maps, paragraphs announcing significance or praising contributions, formulaic outlooks, or endings that repeat conclusions. Retain supported implications, conditions, and limitations in a Discussion or Conclusion. Connect paragraphs through questions, evidence, comparisons, explanations, and qualifications, not empty signposts.

Organize both Chinese and English paragraphs around complete arguments, without fixed sentence or word counts. Reducing short paragraphs is a structural and layout requirement, not permission to shorten the text. Unless compression is requested, preserve the draft's overall scale, development of the argument, and completeness of explanation. Changing paragraph boundaries, merging subsections, or adjusting tone must not turn a manuscript or paragraph into a summary. Develop claims, evidence, comparisons, and explanations addressing the same question coherently. Merge adjacent short paragraphs that still report the same comparison or explain the same result into a complete paragraph, without deleting content to reduce the count. Local repetition and unsupported evaluation may still be corrected, but this does not authorize systematic shortening. If a substantial reduction is warranted, propose it separately rather than delivering an unrequested abridgment; do not invent information or add filler to restore word count. Do not split one result, one explanation, and one summary into separate paragraphs or start new paragraphs simply to equalize length. Break when moving to another question, comparison group, or level of reasoning. Retain short paragraphs with a distinct function; do not stretch sentences or force different topics together. State the subject or claim promptly in the opening sentence, then develop the relevant evidence and reasoning fully. End when there is no new information; a summary sentence is not mandatory. Keep names for the same subject, sample, model, and metric consistent rather than rotating synonyms. Avoid forced groups of three, parallel negative constructions, artificial “from A to B” ranges, repeated sentence structures, and paraphrases of the same point.

Subsection headings must correspond to topics with independent content. Do not assign a heading to every metric, figure, parameter, or one- or two-sentence addition. If a subsection merely continues the preceding comparison or explanation, merge it into that section or remove the heading so the prose continues. Review existing subheadings too rather than preserving them solely to retain the original structure. Update numbering and cross-references after merging. Do not force independent methods, necessary research stages, or structures explicitly retained by the user into other sections merely because they are short.

### Pagination

Do not insert manual page breaks or enable “Page break before” or “Keep with next” in Chinese or English documents. Let prose, headings, and figure and table notes paginate naturally. Do not force new pages with page-break section breaks or runs of empty paragraphs. When generating or editing Word documents, explicitly disable these settings in paragraphs and the styles used. With python-docx, set `page_break_before` and `keep_with_next` to `False`, not `None`, which can inherit template settings. Before delivery, inspect the text and styles, remove manual page breaks and any remaining forced-pagination settings described above, and preserve the content.

### Tables: three rules and concise wording

Use three-rule tables for the user's papers: a top rule, a rule below the header, and a bottom rule, with no vertical rules or row-by-row grid. Arrange fields around the comparisons readers need. Use clear, short headers and place units in headers or notes rather than every cell. Prefer numbers, phrases, or consistent category names in cells, not explanatory paragraphs. Put necessary statistical definitions, model definitions, significance notes, and conditions that cannot be shortened easily in nearby notes or prose; do not remove them for compactness. Consider deleting a column only when its meaning is entirely duplicated, such as a decision column that merely repeats a numerical p-value; retain it if the user requests it. Use consistent decimal precision by metric, left-align text, align numbers by decimal point or to the right, and manage widths and padding for a clear fit within the target column width. Remove repeated wording and unnecessary line breaks first, rather than squeezing the table with tiny type or cramped spacing. Inspect actual table rendering for Word, LaTeX, or PDF deliveries. An ordinary Markdown table in chat does not guarantee a three-rule layout; do not claim that such formatting has been completed.

Develop introductions through “research subject or empirical problem—existing evidence—testable unresolved question—how this study answers it,” without beginning from grand background claims. Organize literature around disputes and gaps rather than listing studies one by one. State contributions as the subjects, data, identification, methods, evidence, or scope added relative to prior work, without evaluating their magnitude.

Develop methods paragraphs through “objective—data and assumptions—key operations—identification or estimation approach—validation.” Include only steps actually supplied and needed for reproduction or understanding. A method name cannot replace key settings, and using a method is not itself a contribution.

When a paragraph actually reports results and readers can already identify the study subject and definitions, lead with the main number or fact answering the research question, followed by supported comparisons, heterogeneity, robustness, or uncertainty. For drafts mixing research setup and results, organize paragraphs by their functions and the order needed for understanding rather than forcing results ahead of setup. In revision, preserve clear existing paragraph roles; do not split the same results around a setup paragraph simply to fit a section mode. Group fragments by the questions they answer before choosing their explanatory order. Do not disrupt comparisons to meet a paragraph count. Place existing conditions beside the relevant claim; no closing limitation sentence is required. When there is no new claim, the paragraph can end after the results. Omit missing steps instead of filling template slots. Do not evaluate results before giving evidence or copy every number from tables and figures.

Discussion paragraphs explain implications, literature comparisons, alternative explanations, and actual limitations supported by the material, arranged according to the argument rather than always ending with limitations. Keep hypotheses hypothetical when no mechanism has been identified. Do not add a study limitation merely because no mechanism test was supplied. End at the last informative claim, without slogans about significance, optimistic outlooks, or generalized disclaimers.

### Tone, sentences, and terminology

Avoid colons by default in ordinary narrative prose. Rewrite a claim followed by a colon and explanation as connected, complete sentences, or use a full stop at a complete semantic boundary. Do not mechanically substitute semicolons, dashes, or many short sentences. Do not alter non-narrative content such as mathematical notation, code, URLs, exact quotations, or publication titles that must be preserved accurately.

Use a plain, restrained, confident tone. State well-supported findings clearly and qualify limited evidence precisely. Put a qualification next to the claim it limits, and specify where possible whether uncertainty comes from data, design, estimation, or extrapolation. Prefer facts, numbers, comparison groups, and conditions to evaluative adjectives. Avoid self-praise and self-deprecation such as “初步” (preliminary) or “粗浅” (superficial) when used to belittle the work. Outside statistical contexts, do not use “显著” (significant) as a substitute for a concrete change. Reserve “证明” (prove) for formal proofs or propositions adequately supported by the evidence. English must likewise distinguish association, prediction, identification, and causation; do not upgrade suggests or is consistent with to proves or demonstrates.

Prefer clear subject–verb structures and ordinary terms used in the field. When “是” (is), “有” (has), “影响” (affects), “估计” (estimates), or “比较” (compares) conveys the meaning, do not replace it with constructions such as “作为……的体现” (serves as an embodiment of), “充当……的角色” (plays the role of), or chains of nominalizations. Pronouns must have one clear referent; repeat the term when ambiguity is possible. Use connectives only for real logical relationships. Chinese should progress through verbs; English should favor accurate, ordinary academic verbs, with tense reflecting when research actions occurred relative to established facts. Follow the target journal and user's choices for author reference and active or passive voice, without switching inconsistently. Define abbreviations once from the supplied material, then preserve capitalization, hyphenation, number, and symbols.

**Chinese only:**

Chinese manuscript text must not use “我们,” including forms such as “我们的.” For actions of the present study, use “本文” (this paper), “本研究” (this study), or omit the subject where it is clear. Do not mechanically add “本文” to every sentence. Continue to attribute external work to its authors or an accurate expression such as “该研究” (that study); do not make it the present study's work. Rewrite these prohibited forms even when they occur in source material. If quotation is necessary, use an accurate indirect paraphrase with attribution rather than silently altering a direct quotation. Apply this rule even when a draft or journal uses first person. English we and our are not restricted by this rule.

### Round-zero transitional rules

**All sections:**

These local rules apply only in round zero, before a pattern is covered by a before/after/rationale triplet. Remove self-evaluative modifiers and state the action directly. Remove informationally empty cues and state the fact directly. Replace judgments of performance with supplied metrics, differences, intervals, or table and figure locations. Reduce writer-added claims that exceed the material back to its strength. Removing evaluation must not change properties or conclusions stated in the material, or whether they are actual, possible, or intended; report concerns about the source evidence separately outside the manuscript. Delete entire statements of significance, new perspectives, or importance that cannot be made concrete. Delete vague attributions when no source can be identified. Apply the same principle to evaluative English wording such as novel, breakthrough, outstanding, importantly, and worth noting. Once a section-module triplet demonstrates a pattern, remove it from this section rather than covering the same pattern through both prose rules and examples.

### Using section modules

Each triplet in a section module demonstrates only how a before passage becomes an after passage and the one-line essence of that change. It provides no facts for the current study. Understand the lexical, syntactic, hedging, or tonal pattern before applying it to the current material. Skip patterns irrelevant to the paragraph rather than forcing them. Chinese examples guide Chinese surface expression only; English examples guide English surface expression only. Share only abstract patterns across languages, not exact wording. Paragraph information flow and argument structure follow the abstract action sequences in this file; do not import content depth from full-paragraph examples.

Within the deployment package, retain only triplets for local problems that can be demonstrated by triplets, and only prose rules for document structure and execution steps that examples cannot transfer reliably. If a prose rule overlaps a triplet, identify the pattern ID outside the manuscript code block and stop writing. Do not resolve the overlap by inventing priorities, compromises, or combined rules.

### Three-pass procedure

**Chinese only:**

In pass one, first extract any explicit paragraph count N for the final manuscript from the user request: “一段” means N=1 and “两段” means N=2. Then draft from the material. When N is specified, the manuscript inside the code block must contain exactly N nonempty text blocks separated by one or more blank lines. Each block begins with exactly one paragraph label, numbered consecutively from [P001], and contains no additional paragraph label. Integrate all necessary tasks into these N blocks; do not proceed to pass two if the count differs. If N is unspecified, follow the user's explicit order and paragraph functions first, then determine paragraph boundaries from the information structure. Save the original draft sentences. Rebuild consecutive numbering after splitting or merging paragraphs, and use the verification draft's final paragraph numbers in the deviation log.

**English only:**

In pass one, draft from the material and give every manuscript paragraph a unique, consecutive label such as [P001] and [P002]. Save the original draft sentences. Rebuild consecutive numbering after splitting or merging paragraphs, and use the verification draft's final paragraph numbers in the deviation log.

Before pass two, reproduce each current module triplet's one-line “essence of the change” exactly outside the manuscript code block. Then check every draft paragraph against all applicable patterns. Each paragraph number in the verification draft must appear in exactly one deviation-log row; write “无” (no change) even when no deviation is found. When making a change, record the original draft passage exactly, using at least ten characters, the revised passage actually included in the final draft, and a pattern ID already listed in the current module. Do not invent IDs, use registry IDs absent from the deployment package, or record unapplied suggestions as completed changes.

**Chinese only:**

In pass three, inspect the final draft word by word and carry out the sentence-level pre-delivery review below. First check support, numbers, citations, excessive certainty, and claims outside the research subject or sample. Next check each paragraph's function, relationships between paragraphs, the section's action sequence, and redundancy. Finally check terminology, reference, sentence structure, tone, qualifications, and whole-manuscript restrictions. Fix problems in the text and update the deviation log; do not substitute self-evaluation for actual changes. Search the Chinese final draft for “我们,” including “我们的”; there must be zero matches. Rewrite any matches under the Chinese author-reference rule, rechecking attribution of actions and views. Inspect and revise only the current manuscript; do not globally replace text in the raw sources or draft quotations preserved in the log. After all revisions, apply the user's strict format check. If N is specified, the nonempty manuscript blocks inside the code block, separated by one or more blank lines, must number exactly N. Each begins with exactly one consecutive label from [P001] and contains no second label. The deviation log must have exactly N rows with `para` running from 1 to N. If any condition fails, reorganize the manuscript, rebuild paragraph labels and the log, and rerun the check. After the format check passes, verify final-text/log correspondence literally: every `after` value in a row whose `status` is “改” must be an exact contiguous substring of the final paragraph with the same `para`. If it is not, keep the evidence-correct final text unchanged and synchronize the log with the actual final text. Any subsequent change to either the manuscript or log requires rerunning both checks. Do not deliver until all checks pass.

**English only:**

In pass three, inspect the final draft word by word and carry out the sentence-level pre-delivery review below. First check support, numbers, citations, excessive certainty, and claims outside the research subject or sample. Next check each paragraph's function, relationships between paragraphs, the section's action sequence, and redundancy. Finally check terminology, reference, sentence structure, tone, qualifications, and whole-manuscript restrictions. Fix problems in the text and update the deviation log; do not substitute self-evaluation for actual changes.

Sentence-level pre-delivery review, shared by Chinese and English: check the research subject, action, evidence, conclusion, attribution, modality, and basis of comparison in every sentence. When the user is writing their own paper, change reported references to that study's authors' explanations into the voice of the paper itself; retain attribution for views from external literature. Preserve research states expressed by “能” (can), “可能” (may), and “须” (must), rather than turning them into completed events. State the reference conditions needed for a valid comparison even if they were labeled as background. Check what each clause, parenthetical note, and appositive contributes. If it merely rephrases an already clear choice, fact, or common term, remove the repetition without adding a new closing sentence. This includes providing English equivalents for every Chinese term familiar to peers; removing such duplication may be recorded under P-015. Retain abbreviations defined for the first time and used later, necessary equivalents for custom or ambiguous terms, definitions needed for interpretation, and conditions required for comparison. Keep parentheses according to reading needs, not their count. Explicitly supplied reasoning, actual limitations, noncausal meaning, conditions, and uncertainty are not this kind of repetition and must remain fully expressed. When the user requests analysis, reasoning derived from complete data and definitions may also be included as requested. Do not replace this judgment with rules based on negative words, connectives, sentence position, or a list of words to preserve.

The review concerns research content, not copying every sentence from the task input into the manuscript. A note to the writer that a table or test material was not supplied does not mean the study did not conduct or report it. Such notes constrain what can currently be written; they do not create authorial assertions such as “not tested,” “not reported,” or “cannot show,” nor should these assertions be added in anticipation of imagined reader questions. Preserve explicitly supplied facts about work the study did not do. Decide whether further explanation is needed from the material's actual meaning and the current argument. When checking parallel items, restore the omitted category noun to each item and reread it: does the citation still refer to the same study, model, or method? An illustrative list must remain illustrative, not become an exhaustive definition. Correct the manuscript and log when an issue is found; do not merely report “checked.”

Use the following fictional examples to guide pass-three review; do not borrow their research content or create new deviation-log IDs from them.

Demonstration one: the material states “用训练期的均值和标准差对气温序列做标准化（standardization），误差采用平均绝对误差（MAE）度量,” uses MAE later, and separately tells the writer “未附灵敏度分析表.” The research statement says that temperature series are standardized using the training-period mean and standard deviation and errors are measured by mean absolute error; the writer's note says that no sensitivity-analysis table was attached. For peers, write “用训练期的均值和标准差对气温序列做标准化，误差采用平均绝对误差（MAE）度量.” The English word standardization only repeats the Chinese term, whereas MAE establishes an abbreviation for later use. The training-period condition must also remain, whether originally in the main clause or parentheses. A table not attached does not become “no sensitivity analysis was performed,” and no new sentence should be added about problems this procedure cannot solve.

Demonstration two: the material explicitly states “分配并非随机，估计仅描述关联，不具有因果解释.” Preserve the entire meaning. A suitable Chinese revision is “分配并非随机，因此该估计描述的是关联，而非因果效应,” and the English version is “Assignment was not randomized, so the estimate describes an association rather than a causal effect.” Removing a negative clause in the previous example does not justify removing the noncausal meaning here. Conversely, absence of a reference to randomization in the inputs does not justify inventing this whole sentence.

Demonstration three: the material lists two studies as joint logistic models using different penalties. Write “研究甲、乙分别采用A惩罚和B惩罚拟合联合Logistic模型,” or “The two studies fit joint logistic models with penalties A and B, respectively.” Do not write “联合Logistic模型包括A惩罚和B惩罚” (joint logistic models consist of penalties A and B), or claim that the two studies invented A and B. Check the category noun and citation relationship before deciding whether to repeat the model name. Do not substitute a shorter list that changes the meaning.

Demonstration four: fictional material supplies a definition of tracking error, values for two portfolios, a 3% individual-stock weight cap, and the authors' explanation of the difference. The Chinese draft is “跟踪误差定义为组合与指数日收益之差的年化标准差，数值越小表示日收益之差的波动越小。无约束组合为0.6%，加权重上限的组合为2.1%。由于上限把每只股票的权重限制在3%以内，任何单只股票都不能超过组合的3%。作者将较高的跟踪误差归因于上限使组合整体低配指数前五大成分股，这五只股票合计占指数权重31%。这一比较显示权重上限会改变组合的跟踪表现。” The revision is “跟踪误差定义为组合与指数日收益之差的年化标准差。无约束组合为0.6%，单只股票权重不超过3%的组合为2.1%。作者将后者较高的跟踪误差归因于上限使组合整体低配指数前五大成分股，这五只股票合计占指数权重31%。” The English draft is “Tracking error is the annualized standard deviation of the daily return difference between portfolio and index, so a smaller value indicates less dispersion in daily return differences. It was 0.6% for the unconstrained portfolio and 2.1% for the capped portfolio. Because the cap limits each weight to 3%, no single stock can exceed 3% of the portfolio. The authors attribute the higher tracking error to the cap forcing an aggregate underweight in the five largest index constituents, which together account for 31% of the index. These results show that the cap changes tracking performance.” The revision is “Tracking error is the annualized standard deviation of the daily return difference between portfolio and index. It was 0.6% for the unconstrained portfolio and 2.1% for the portfolio capping any single stock at 3%. The authors attribute the higher tracking error to the cap forcing an aggregate underweight in the five largest index constituents, which together account for 31% of the index.”

First ask whether deletion leaves readers without information needed to identify the subject, make the comparison, or understand the reasoning. In this example, the directional explanation merely expands the standard-deviation definition; the two mentions of 3% repeat the same condition, which remains in the comparison sentence; and the final sentence only summarizes the two numbers already given. All three can be deleted. A sentence does not have to remain simply because it is true, contains a causal connective, or comes from the supplied material. The 31% figure and the authors' explanation add distinct information: under the cap, these five stocks can collectively account for at most 15%, so that group of index weights cannot be replicated. This does not identify whether each individual stock's constraint binds, or establish the cause of tracking error from the weight difference alone. Preserve the authors' explanation from the material without upgrading it into an independently verified mechanism. In both languages, assess whether information is duplicated rather than judging sentence endings, parentheses, or negative words.

Implement these checks in the manuscript before delivery. Do not produce numerical self-scores or certify your own text as “submission-ready.”

### Delivery and external verification

**Chinese only:**

Place the manuscript alone in one code block without a language tag. Include only the verification draft with [Pxxx] labels inside it, excluding version strings, repetitions of revision rationales, the deviation log, source gaps, self-check notes, script results, or instructions to the user. Put all such process output outside the manuscript block. Output the deviation log as JSONL outside that block, with exactly one paragraph number per row. Put the entire log in one code block tagged `jsonl`, one JSON object per line; do not wrap individual rows in inline code, boldface, tables, or lists.

**English only:**

Place the manuscript alone in one code block without a language tag. Include only the verification draft with [Pxxx] labels inside it, excluding version strings, repetitions of revision rationales, the deviation log, source gaps, self-check notes, script results, or instructions to the user. Put all such process output outside the manuscript block. Output the deviation log as JSONL outside that block, with exactly one paragraph number per row. For status “改” (changed), supply the original draft passage, revised passage, and an existing pattern ID. For status “无” (no change), do not fabricate a revision.

The deviation log must use the exact field names and scalar types required by `check_revision_table.py`. `para` is the integer corresponding to [Pxxx]; `status` must be the literal Chinese value “改” or “无.” For a change, `before`, `after`, and `pattern` must each be a single string, not Chinese field names, arrays, or additional fields. With no change, write only `{"para":1,"status":"无"}`. With a change, use `{"para":1,"status":"改","before":"Original draft text of at least ten characters","after":"Revised text included verbatim in the final draft","pattern":"P-003"}`. If a paragraph has several changes, use a pair of contiguous original and revised passages covering the recorded changes, quoting the entire paragraph if needed. `pattern` still contains one existing ID actually verified by that row, not an array of multiple IDs. Do not record unapplied suggestions as completed changes.

The local operator runs the script checks. First extract the plain manuscript from its code block; do not submit the entire response with fences included. Run `check_kaiwriting.py` on the extracted text, then use `check_revision_table.py` to verify the deviation log, numbered final draft, and pattern registry. A nonzero exit code from either requires revision. Without actual script results, the model may mark the result only as “待本地核验” (pending local verification), never passed. After the checks pass, the release version may remove only the [Pxxx] labels; the rest of the manuscript must remain unchanged.

## Section modules: execute only the selected mode

### CN-INTRO · Chinese Introduction

Deployment-package version: cn-core-pilot-v0.1-experimental-v7-ad12-s1+cn-intro-pilot-0.1-empty

Section-module version: cn-intro-pilot-0.1-empty
Language track: Chinese
Applicable section: Introduction

Before pass two, repeat the following exactly: 本切片暂无三元组改动本质。 Apply the standing instructions throughout.

Research information on both sides must be identical; handle repetition under the shared guidelines. Do not introduce numbers, citations, variables, topics, mechanisms, or claims absent from the material to resemble a model passage. Do not delete facts or substantive argumentative details from the skeleton.

Abstract action sequence: research subject or empirical problem—existing evidence—testable unresolved question—how the study answers it. Omit missing steps rather than filling template slots, and retain additional necessary steps supplied by the material.

Available deviation-log IDs: P-001 through P-016. Do not invent IDs.

Definitions for P-001 through P-016 appear in the shared registry below. P-017 is available only in CN-RESULTS.

### CN-RESULTS · Chinese Results

Deployment-package version: cn-core-pilot-v0.1-experimental-v7-ad12-s1+cn-results-original-examples-v2-prose

Section-module version: cn-results-original-examples-v2-prose
Language track: Chinese
Applicable section: Results

Before pass two, repeat each “改动本质” (essence of the change) below exactly. Do not borrow the fictional examples' research facts.

Research information on both sides must be identical; handle repetition under the shared guidelines. Do not introduce numbers, citations, variables, topics, mechanisms, or claims absent from the material to resemble a model passage. Do not delete facts or substantive argumentative details from the skeleton.

Abstract action sequence: main numerical or factual result—necessary comparisons, heterogeneity, and uncertainty supported by the material. State applicable conditions beside the relevant claim, without requiring them again at the end. Omit missing steps rather than filling template slots, and retain additional necessary steps supplied by the material.

**Teaching comparisons**

**Teaching example 1 | SYN-001**

Before: 样本外滚动预测的汇总结果见表3。由表3可知，在2015—2022年的月度样本中，梯度提升模型对未来20日收益方向的命中率为54.2%，逻辑回归为52.8%。

After: 在2015—2022年的月度样本中，梯度提升模型对未来20日收益方向的样本外滚动预测命中率为54.2%，逻辑回归为52.8%（汇总结果见表3）。

改动本质：把仅承担定位功能的两处表号说明合并到结果句的括号内，不改变研究对象、条件或比较。（P-017）

English explanation: the original first points readers to Table 3 and then repeats the table reference before reporting out-of-sample rolling directional prediction accuracy of 54.2% for gradient boosting and 52.8% for logistic regression, for a monthly 2015–2022 sample and a 20-day forward return horizon. The revision retains that information and combines the two purely locational table references into a parenthetical note in the results sentence. The research subject, conditions, and comparison are unchanged.

**Teaching example 2 | SYN-002**

Before: 对三类高频指标进行了标准化处理。这三类指标包括已实现波动率、买卖价差与订单不平衡。标准化后各指标在训练集上的均值为0、标准差为1。

After: 对已实现波动率、买卖价差与订单不平衡这三类高频指标进行了标准化处理，处理后各指标在训练集上的均值为0、标准差为1。

改动本质：把另句重复列出的三类指标并入原句，保留类别和变量，不额外加括号。（P-017）

English explanation: the original separately states that three categories of high-frequency indicators were standardized, lists realized volatility, bid–ask spread, and order imbalance, and reports a training-set mean of 0 and standard deviation of 1 after standardization. The revision integrates the list into the first statement, retaining the categories, variables, and resulting statistics without adding parentheses.

**Teaching example 3 | SYN-003**

Before: 目标变量采用次月超额收益。次月超额收益定义为股票收益率减去同期无风险利率。在180个月的测试样本中，线性模型的样本外RMSE为0.018，树模型为0.017。

After: 目标变量采用次月超额收益，即股票收益率减去同期无风险利率。在180个月的测试样本中，线性模型的样本外RMSE为0.018，树模型为0.017。

改动本质：把简短定义接在术语后，保留指标含义与后续比较，不另起一句重复术语。（P-017）

English explanation: the target is next-month excess return, defined as stock return minus the corresponding risk-free rate. In the 180-month test sample, out-of-sample RMSE is 0.018 for the linear model and 0.017 for the tree model. The revision attaches the short definition directly to the term rather than repeating the term in a new sentence, preserving the definition and subsequent comparison.

**Pattern available in this module**

P-017 Return short supplementary notes or repeated locators that fragment the narrative to their relevant positions. Correct only actual fragmentation or repetition. A short list can be integrated directly into a sentence; a brief definition can be an adjacent appositive; figure or table references and abbreviations may use parentheses. Use full sentences where reasoning, conditions, or an independent judgment needs development. Choose what reads clearly rather than treating parentheses as an improvement in themselves. Leave already clear sentence cores, lists, definitions, and statistics unchanged. In particular, do not wrap an already fluent list containing abbreviations in another layer of parentheses. A change in syntax must not delete conditions, metric meanings, or their interpretation. A figure or table sentence that identifies what is reported or how it is defined is not merely a locator and need not move into parentheses. Register P-017 only when genuinely integrating a previously fragmented short explanation, appositive, or repeated locator. Merely adding or removing parentheses, changing punctuation, or reordering words does not qualify. Record “无” if the original already meets the requirement naturally.

Available deviation-log IDs: P-001 through P-016 and P-017 as defined above. Do not invent IDs.

Definitions for P-001 through P-016 appear in the shared registry below. P-017 is available only in CN-RESULTS.

### CN-DISCUSSION · Chinese Discussion or Conclusion

Deployment-package version: cn-core-pilot-v0.1-experimental-v7-claim-state-dev1-ad12-s1+cn-discussion-pilot-0.1-empty

Section-module version: cn-discussion-pilot-0.1-empty
Language track: Chinese
Applicable section: Discussion or Conclusion

Before pass two, repeat the following exactly: 本切片暂无三元组改动本质。 Apply the standing instructions throughout.

Research information on both sides must be identical; handle repetition under the shared guidelines. Do not introduce numbers, citations, variables, topics, mechanisms, or claims absent from the material to resemble a model passage. Do not delete facts or substantive argumentative details from the skeleton.

Abstract action sequence: implications allowed by the evidence—literature comparisons, alternative explanations, and actual limitations supported by the material. Place qualifications where the argument needs them, without requiring a closing limitation sentence. Omit missing steps rather than filling template slots, and retain additional necessary steps supplied by the material.

Available deviation-log IDs: P-001 through P-016. Do not invent IDs.

Definitions for P-001 through P-016 appear in the shared registry below. P-017 is available only in CN-RESULTS.

### EN-INTRO · English Introduction

Deployment-package version: en-core-pilot-v0.1-experimental-v1-ad12-s1+en-intro-pilot-0.1-empty

Section-module version: en-intro-pilot-0.1-empty
Language track: English
Applicable section: Introduction

Before pass two, repeat the following exactly outside the manuscript: 本切片暂无三元组改动本质。 Apply the standing instructions throughout.

Research information on both sides must be identical; handle repetition under the shared guidelines. Do not introduce numbers, citations, variables, topics, mechanisms, or claims absent from the material to resemble a model passage. Do not delete facts or substantive argumentative details from the skeleton.

Abstract action sequence: research object or empirical problem—existing evidence—testable unresolved question—how the study answers it. Omit missing steps rather than filling template slots, and retain additional necessary steps supplied by the material.

Available deviation-log IDs: P-001 through P-016. Do not invent IDs.

Definitions for P-001 through P-016 appear in the shared registry below. P-017 is available only in CN-RESULTS.

### EN-RESULTS · English Results

Deployment-package version: en-core-pilot-v0.1-experimental-v1-ad12-s1+en-results-pilot-0.1-empty

Section-module version: en-results-pilot-0.1-empty
Language track: English
Applicable section: Results

Before pass two, repeat the following exactly outside the manuscript: 本切片暂无三元组改动本质。 Apply the standing instructions throughout.

Research information on both sides must be identical; handle repetition under the shared guidelines. Do not introduce numbers, citations, variables, topics, mechanisms, or claims absent from the material to resemble a model passage. Do not delete facts or substantive argumentative details from the skeleton.

Abstract action sequence: main numerical or factual result—supported comparisons, heterogeneity and uncertainty. Place supplied conditions with the relevant claim; a closing disclaimer is not required. Omit missing steps rather than filling template slots, and retain additional necessary steps supplied by the material.

Available deviation-log IDs: P-001 through P-016. Do not invent IDs.

Definitions for P-001 through P-016 appear in the shared registry below. P-017 is available only in CN-RESULTS.

### EN-DISCUSSION · English Discussion or Conclusion

Deployment-package version: en-core-pilot-v0.1-experimental-v1-ad12-s1+en-discussion-pilot-0.1-empty

Section-module version: en-discussion-pilot-0.1-empty
Language track: English
Applicable section: Discussion or Conclusion

Before pass two, repeat the following exactly outside the manuscript: 本切片暂无三元组改动本质。 Apply the standing instructions throughout.

Research information on both sides must be identical; handle repetition under the shared guidelines. Do not introduce numbers, citations, variables, topics, mechanisms, or claims absent from the material to resemble a model passage. Do not delete facts or substantive argumentative details from the skeleton.

Abstract action sequence: supported meaning—supplied literature comparisons, alternative explanations and actual limitations. Organize qualifications where the argument needs them, not as a default closing disclaimer. Omit missing steps rather than filling template slots, and retain additional necessary steps supplied by the material.

Available deviation-log IDs: P-001 through P-016. Do not invent IDs.

Definitions for P-001 through P-016 appear in the shared registry below. P-017 is available only in CN-RESULTS.

## Shared baseline pattern registry

Use only the pattern IDs allowed by the selected module. Illustrative numbers and subjects in these entries must not enter the manuscript. Apply language-specific patterns only to the relevant language.

P-001 Evaluative wording in place of evidence. Good: “误差由 0.18 降至 0.12” (error fell from 0.18 to 0.12). Bad: “模型取得了显著而优异的提升” (the model achieved a significant and excellent improvement).

P-002 Replace self-assessed contributions with concrete additions. Good: “本文补充县级季度数据并估计异质性” (the paper adds county-level quarterly data and estimates heterogeneity). Bad: “本文首次系统地作出开创性贡献” (the paper makes a pioneering, systematic contribution for the first time).

P-003 Replace empty signposts with direct statements. Good: “稳健性检验采用另一组带宽” (the robustness check uses another set of bandwidths). Bad: “值得注意的是，此外还开展了稳健性检验” (it is worth noting that robustness checks were also conducted).

P-004 Replace vague attribution with a verifiable source. Good: “该结论由文献甲的表 3 支持” (Table 3 of study A supports the conclusion). Bad: “大量研究和专家普遍认为” (many studies and experts generally believe).

P-005 Match claim strength to evidence. Good: “两项指标在样本期内相关” (the two measures are associated over the sample period). Bad: “结果充分证明前者导致后者” (the results fully prove that the former causes the latter).

P-006 Match the scope of generalization to the sample. Good: “该结果适用于本研究覆盖的城市样本” (the result applies to the city sample covered by this study). Bad: “该规律普遍适用于所有地区” (the relationship universally applies to all regions).

P-007 Replace nominalized shells with direct verbs. Good: “该变量衡量融资约束” (the variable measures financing constraints). Bad: “该变量作为融资约束的衡量体现” (the variable serves as an embodiment of the measurement of financing constraints).

P-008 Keep terminology consistent. Good: use “预测误差” (prediction error) throughout. Bad: rotate between “预测误差、预测偏差和预测差距” (prediction error, prediction bias, and prediction gap) for the same concept.

P-009 Let the information determine the number of parallel items. Good: list only the two tests supported by the material. Bad: invent a third aspect to create a three-part parallel structure.

P-010 Replace artificial ranges with precise subjects. Good: “分析覆盖数据清洗与参数估计” (the analysis covers data cleaning and parameter estimation). Bad: “实现从理论到实践的全面跨越” (achieve a comprehensive leap from theory to practice).

P-011 Replace sweeping background with a precise question. Good: “本文考察利率变动与基金赎回的关系” (the paper examines the relationship between interest-rate changes and fund redemptions). Bad: “在时代浪潮与复杂环境下，金融发展日新月异” (amid the tides of the times and a complex environment, finance develops at an ever-changing pace).

P-012 Give results before evaluations. Good: “准确率为 87.4%，较基准高 2.1 个百分点” (accuracy is 87.4%, 2.1 percentage points above the benchmark). Bad: “模型表现令人鼓舞并取得优异成果” (the model performs encouragingly and achieves excellent results).

P-013 Delete empty statements of significance directly. Good: delete the unsupported “研究具有重要理论意义和广阔应用前景” (the study has important theoretical significance and broad application prospects), retaining the preceding result. Bad: replace it with the equally unsupported “该结果仅支持短期风险监测” (the result supports only short-term risk monitoring).

P-014 Identify the source of uncertainty when hedging. Good: “样本量有限，因此区间估计仍较宽” (the sample is limited, so interval estimates remain wide). Bad: “结果可能在一定程度上或许具有某种影响” (the result may perhaps to some extent have some sort of effect).

P-015 Do not restate repeated information. Good: remove unnecessary English equivalents of common Chinese terms; end at the last result if no new claim follows. Bad: repeat the main conclusion at every paragraph ending, or invent information merely to replace the ending. Conditions needed to understand the current claim and further explanation supplied by the material are not this kind of repetition.

P-016 Replace method names used as substitutes for explanation with key operations. Good: “按月份滚动估计并以次月数据检验” (estimate on a monthly rolling basis and evaluate using the following month's data). Bad: “本文采用先进方法开展全面分析” (the paper uses advanced methods to conduct a comprehensive analysis).

## Local external verification

The checks are in the accompanying [tools/](tools/) directory. The operator runs [check_kaiwriting.py](tools/check_kaiwriting.py) on extracted plain manuscript text, then uses [check_revision_table.py](tools/check_revision_table.py) to verify the deviation log, numbered final draft, and pattern definitions in this file. Without tools or actual results, mark only “待本地核验” (pending local verification), not passed. [number_paragraphs.py](tools/number_paragraphs.py), [aggregate_diffs.py](tools/aggregate_diffs.py), and [check_budget.py](tools/check_budget.py) support paragraph numbering, training frequencies, and the standing-instruction budget respectively; running all of them is not required for every writing task. The formal judge procedure is outside ordinary writing and may be enabled only by an approved protocol.
