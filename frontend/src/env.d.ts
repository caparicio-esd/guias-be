/// <reference types="astro/client" />

export interface GuiaGet {
    id:           number;
    title:        string;
    description:  string;
    identifiers:  Identifiers;
    coordinator:  Coordinator;
    teachers:     Coordinator[];
    results:      any[];
    competencies: any[];
    hours:        Hours;
    methodology:  Methodology;
    evaluation:   EvaluationClass;
    calification: Calification;
    chronogram:   Chronogram;
    resources:    any[];
}

export interface Calification {
    continual_evaluation:     Evaluation;
    ordinary_evaluation:      number;
    extraordinary_evaluation: number;
    disabled_evaluation:      Evaluation;
}

export interface Evaluation {
    theory:    number;
    practical: number;
    attitude:  number;
}

export interface Chronogram {
    id:         number;
    blocks:     Block[];
    created_at: Date;
    updated_at: Date;
}

export interface Block {
    id:               number;
    time_entity:      number;
    block:            number;
    theme:            number;
    exercise:         Exercise;
    exercise_content: string;
    competencies:     string;
    exam:             null;
    special_activity: null;
    created_at:       Date;
    updated_at:       Date;
    chronogram:       number;
}

export enum Exercise {
    Blabla = "blabla",
}

export interface Coordinator {
    id:       number;
    username: string;
    email:    string;
}

export interface EvaluationClass {
    instruments: Methodology;
    criteria:    Methodology;
}

export interface Methodology {
    theory:    null;
    practical: null;
    others:    null | string;
}

export interface Hours {
    activities:  number;
    probes:      number;
    selfwork:    number;
    preparation: number;
}

export interface Identifiers {
    type:           string;
    character:      string;
    specialty:      Specialty;
    subject:        string;
    course:         string;
    semester:       string;
    credits:        number;
    hours_presence: number;
    department:     string;
    prelation:      string;
    language:       string;
}

export interface Specialty {
    id:          number;
    title:       string;
    description: string;
}
