# alfianlosari/appclipcodegenerator

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 71618a34e319 @ 651099e8db24da98

## Summary (orientation draft, not independently verified)

A macOS SwiftUI app for generating App Clip Codes, with color/NFC/logo customization and SVG/PNG export, depending on Apple's App Clip Generator CLI and librsvg.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project is licensed under the MIT license and authored by Alfian Losari. -- evidence: [README.md#L32-L32](https://github.com/alfianlosari/AppClipCodeGenerator/blob/71618a34e319ab554aa7773d5bb5ac04bed4e694/README.md#L32-L32), [README.md#L36-L36](https://github.com/alfianlosari/AppClipCodeGenerator/blob/71618a34e319ab554aa7773d5bb5ac04bed4e694/README.md#L36-L36)
- components (1 claim(s)):
  - [observation/documented] The app is built using SwiftUI and targets macOS 11 Big Sur and above. -- evidence: [README.md#L7-L12](https://github.com/alfianlosari/AppClipCodeGenerator/blob/71618a34e319ab554aa7773d5bb5ac04bed4e694/README.md#L7-L12)
- design-choices (2 claim(s)):
  - [observation/documented] Foreground and background colors can be customized via custom colors or Apple-provided templates. -- evidence: [README.md#L7-L12](https://github.com/alfianlosari/AppClipCodeGenerator/blob/71618a34e319ab554aa7773d5bb5ac04bed4e694/README.md#L7-L12)
  - [observation/documented] The generator supports choosing NFC- or camera-only scanning and including or omitting the Apple logo. -- evidence: [README.md#L7-L12](https://github.com/alfianlosari/AppClipCodeGenerator/blob/71618a34e319ab554aa7773d5bb5ac04bed4e694/README.md#L7-L12)
- workflows (1 claim(s)):
  - [observation/documented] Setup involves downloading a release from GitHub and granting the app access via the Privacy panel in System Preferences. -- evidence: [README.md#L16-L19](https://github.com/alfianlosari/AppClipCodeGenerator/blob/71618a34e319ab554aa7773d5bb5ac04bed4e694/README.md#L16-L19)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Users provide a valid App Clip URL code in a text field to generate the code. -- evidence: [README.md#L23-L23](https://github.com/alfianlosari/AppClipCodeGenerator/blob/71618a34e319ab554aa7773d5bb5ac04bed4e694/README.md#L23-L23)
  - [observation/documented] Generated codes can be exported as SVG and PNG images. -- evidence: [README.md#L7-L12](https://github.com/alfianlosari/AppClipCodeGenerator/blob/71618a34e319ab554aa7773d5bb5ac04bed4e694/README.md#L7-L12)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Installation requires Apple's App Clip Generator CLI tool and librsvg (installed via Homebrew). -- evidence: [README.md#L16-L19](https://github.com/alfianlosari/AppClipCodeGenerator/blob/71618a34e319ab554aa7773d5bb5ac04bed4e694/README.md#L16-L19)
  - [observation/documented] The project credits Apple's App Clip Generator CLI Tool and librsvg as external components. -- evidence: [README.md#L27-L28](https://github.com/alfianlosari/AppClipCodeGenerator/blob/71618a34e319ab554aa7773d5bb5ac04bed4e694/README.md#L27-L28)
- limitations (1 claim(s)):
  - [inference/documented] The app appears to be macOS-only, since supported platforms are stated as macOS 11 Big Sur and above. -- evidence: [README.md#L7-L12](https://github.com/alfianlosari/AppClipCodeGenerator/blob/71618a34e319ab554aa7773d5bb5ac04bed4e694/README.md#L7-L12)
- relevance: unknown (no source-linked claim submitted for this facet)

Every claim for this repository is shown above and in [full detail](appclipcodegenerator.detail.md).

Metadata and full claim list: [full detail](appclipcodegenerator.detail.md)
Human notes ([notes](appclipcodegenerator.notes.md), never overwritten by build)

[Back to map index](../../index.md)
