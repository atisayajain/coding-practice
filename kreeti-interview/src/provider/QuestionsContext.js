import { createContext } from 'react';
import QuestionsData from '../data/questions.json';

export const QuestionsContext =createContext({ questions: QuestionsData });