"""Strict shared contracts for files, records, and agent proposals."""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

Access = Literal["public", "internal", "confidential", "restricted"]
Review = Literal[
    "extracted", "mechanically_checked", "human_reviewed", "approved", "disputed", "superseded", "unverified"
]
Profile = Literal["general", "scholarly", "policy-legal", "organizational", "interview", "mixed"]
PageType = Literal["source", "concept", "entity", "finding", "debate", "theme", "gap", "answer"]
EvidenceType = Literal[
    "empirical_result",
    "legal_authority",
    "policy_statement",
    "implementation_guidance",
    "organizational_statement",
    "participant_report",
    "method",
    "definition",
    "recommendation",
    "contextual_fact",
]
Predicate = Literal[
    "supports",
    "contradicts",
    "qualifies",
    "applies_to",
    "duplicates",
    "supersedes",
    "mentions",
    "measures",
    "authored_by",
    "issued_by",
    "derived_from",
]
SourceType = Literal[
    "scholarly_article",
    "book",
    "report",
    "dataset",
    "webpage",
    "legislation",
    "regulation",
    "guidance",
    "standard",
    "organizational_record",
    "interview",
    "session",
    "synthesis_report",
]
EntityType = Literal[
    "person",
    "organization",
    "jurisdiction",
    "instrument",
    "program",
    "concept",
    "method",
    "population",
    "dataset",
    "event",
]
Digest = str


class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid", validate_assignment=True)


class Consent(Strict):
    state: Literal["granted", "pending", "denied"]
    quote: bool
    paraphrase: bool
    identify: bool
    publish: bool


class Origin(Strict):
    title: str = Field(min_length=1)
    identifier: str = Field(min_length=1)
    locator: str = Field(min_length=1)


class Metadata(Strict):
    title: str = Field(min_length=1)
    creator: str = Field(min_length=1)
    date: str | None = None
    source_type: SourceType
    access: Access = "internal"
    identifiers: dict[str, str] = Field(default_factory=dict)
    url: str | None = None
    jurisdiction: str | None = None
    legal_status: str | None = None
    status_date: str | None = None
    provision: str | None = None
    methodology: str | None = None
    population: str | None = None
    venue: str | None = None
    organization: str | None = None
    role: str | None = None
    attribution: str | None = None
    verified_date: str | None = None
    consent: Consent | None = None
    original_sources: list[Origin] = Field(default_factory=list)

    @model_validator(mode="after")
    def profile_rules(self):
        if self.source_type in {"interview", "session"}:
            if not self.consent or self.consent.state != "granted" or not self.consent.paraphrase:
                raise ValueError("RCW_CONSENT_REQUIRED: granted paraphrase consent is required")
            if self.access not in {"confidential", "restricted"}:
                raise ValueError("RCW_ACCESS_POLICY: interview/session requires confidential or restricted")
        if self.source_type in {"legislation", "regulation"}:
            if not all((self.jurisdiction, self.legal_status, self.status_date, self.provision)):
                raise ValueError(
                    "RCW_PROFILE_INVALID: legal sources need jurisdiction, legal_status, status_date, provision"
                )
        if self.url and not self.url.startswith(("https://", "http://")):
            raise ValueError("RCW_URL_INVALID: use an http(s) source URL")
        return self


class SourceRoot(Strict):
    root_id: str = Field(pattern=r"^[a-zA-Z0-9_-]+$")
    path: str
    read_only: Literal[True] = True


class CorpusConfig(Strict):
    schema_version: Literal["1.0"] = "1.0"
    corpus_id: str
    title: str
    profile: Profile = "mixed"
    default_access: Access = "internal"
    source_roots: list[SourceRoot] = Field(min_length=1)
    source_max_bytes: int = Field(default=20_000_000, gt=0)
    quote_max_words: int = Field(default=20, ge=0, le=1000)


class Scope(Strict):
    population: str | None = None
    jurisdiction: str | None = None
    timeframe: str | None = None
    setting: str | None = None
    method: str | None = None
    instrument_status: str | None = None
    qualifiers: str | None = None


class ClaimDraft(Strict):
    key: str = Field(min_length=1)
    text: str = Field(min_length=1)
    slice_ids: list[str] = Field(min_length=1)
    evidence_type: EvidenceType
    scope: Scope = Field(default_factory=Scope)
    polarity: Literal["affirmed", "negated", "mixed", "not_applicable"] = "affirmed"
    extraction_confidence: float = Field(default=0.5, ge=0, le=1)


class EntityDraft(Strict):
    key: str
    name: str = Field(min_length=1)
    entity_type: EntityType
    aliases: list[str] = Field(default_factory=list)
    external_ids: dict[str, str] = Field(default_factory=dict)
    claim_keys: list[str] = Field(min_length=1)


class RelationshipDraft(Strict):
    subject: str
    predicate: Predicate
    object: str
    claim_ids: list[str] = Field(min_length=1)
    rationale: str = Field(min_length=1)


class IngestProposal(Strict):
    schema_version: Literal["1.0"] = "1.0"
    operation_id: str
    claims: list[ClaimDraft]
    entities: list[EntityDraft] = Field(default_factory=list)
    relationships: list[RelationshipDraft] = Field(default_factory=list)


class Assertion(Strict):
    text: str = Field(min_length=1)
    claim_ids: list[str]
    opposing_claim_ids: list[str] = Field(default_factory=list)


class PageDraft(Strict):
    key: str
    title: str = Field(min_length=1)
    page_type: Literal["concept", "finding", "debate", "theme"]
    assertions: list[Assertion] = Field(min_length=1)


class GapDraft(Strict):
    question: str = Field(min_length=1)
    reason: str = Field(min_length=1)
    claim_ids: list[str] = Field(default_factory=list)
    suggested_source: str = "Original primary evidence"


class AnalysisProposal(Strict):
    schema_version: Literal["1.0"] = "1.0"
    operation_id: str
    pages: list[PageDraft]
    relationships: list[RelationshipDraft] = Field(default_factory=list)
    gaps: list[GapDraft] = Field(default_factory=list)


class AnswerProposal(Strict):
    schema_version: Literal["1.0"] = "1.0"
    operation_id: str
    status: Literal["answered", "partially_answered", "conflicted", "insufficient_evidence"]
    assertions: list[Assertion]
    limitations: list[str]


class Envelope(Strict):
    schema_version: Literal["1.0"] = "1.0"
    id: str = Field(pattern=r"^[a-z]+_[0-9a-f]{32,64}$")
    access: Access
    review_state: Review
    created_at: str
    updated_at: str
    created_by_operation: str
    updated_by_operation: str


class Package(Envelope):
    record_type: Literal["package"] = "package"
    key: str
    digest: Digest
    status: Literal["active", "duplicate", "superseded"]
    duplicate_of: str | None = None
    proposal_digest: Digest
    files: list[dict]


class Source(Envelope):
    record_type: Literal["source"] = "source"
    metadata: Metadata
    root_id: str
    path: str


class SourceVersion(Envelope):
    record_type: Literal["source_version"] = "source_version"
    source_id: str
    package_id: str
    digest: Digest
    metadata_digest: Digest
    root_id: str
    path: str
    status: Literal["current", "superseded"]


class Locator(Strict):
    kind: Literal["lines", "html_block"]
    line_start: int = Field(ge=1)
    line_end: int = Field(ge=1)
    heading: str = ""
    ordinal: int = Field(ge=0)


class Slice(Envelope):
    record_type: Literal["slice"] = "slice"
    source_version_id: str
    source_id: str
    locator: Locator
    text_digest: Digest
    excerpt: str | None = None
    quotation_allowed: bool
    publication_allowed: bool


class Claim(Envelope):
    record_type: Literal["claim"] = "claim"
    text: str
    slice_ids: list[str] = Field(min_length=1)
    source_ids: list[str] = Field(min_length=1)
    evidence_type: EvidenceType
    scope: Scope
    polarity: Literal["affirmed", "negated", "mixed", "not_applicable"]
    extraction_confidence: float = Field(ge=0, le=1)
    lineage_status: Literal["original_available", "original_missing"]


class Entity(Envelope):
    record_type: Literal["entity"] = "entity"
    name: str
    entity_type: EntityType
    aliases: list[str]
    external_ids: dict[str, str]
    claim_ids: list[str]
    identity_state: Literal["proposed", "approved"] = "proposed"


class Relationship(Envelope):
    record_type: Literal["relationship"] = "relationship"
    subject: str
    predicate: Predicate
    object: str
    claim_ids: list[str]
    rationale: str


class Page(Envelope):
    record_type: Literal["page"] = "page"
    page_type: PageType
    path: str
    title: str
    aliases: list[str] = Field(default_factory=list)
    claim_ids: list[str]
    source_ids: list[str]
    assertions: list[Assertion]
    maturity: Literal["stub", "draft", "reviewed", "stable"] = "draft"


class Gap(Envelope):
    record_type: Literal["gap"] = "gap"
    question: str
    reason: str
    claim_ids: list[str]
    suggested_source: str
    status: Literal["open", "resolved"] = "open"


class Citation(Envelope):
    record_type: Literal["citation"] = "citation"
    source_id: str
    csl: dict


class Operation(Strict):
    schema_version: Literal["1.0"] = "1.0"
    id: str
    record_type: Literal["operation"] = "operation"
    mode: str
    state: Literal["applied"] = "applied"
    base_digest: str
    inputs_digest: str
    proposal_digest: str
    output_paths: list[str]
    skill_version: str = "0.1.0"
    completed_at: str


TABLES = {
    "packages": Package,
    "sources": Source,
    "source_versions": SourceVersion,
    "slices": Slice,
    "claims": Claim,
    "entities": Entity,
    "relationships": Relationship,
    "pages": Page,
    "gaps": Gap,
    "citations": Citation,
    "operations": Operation,
}


def dump(model):
    return model.model_dump(mode="json", exclude_none=False)
