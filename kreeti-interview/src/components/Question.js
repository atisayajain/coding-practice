import React, { useState } from 'react';

export default function Question({ question, saveAnswer, answerSaved }) {
    const [answer, setAnswer] = useState(null);
    const [checked, setChecked] = useState(null);

    const handleAnswerSelect = (event) => {
        console.log(event.target.name, event.target.value);
        setAnswer(parseInt(event.target.value));
        setChecked(checked);
    }
    
    const onSave = (event) => {
        event.preventDefault();
        console.log(answer);
        saveAnswer(question.id, answer);
    }
    
    return(
        <div className="w-full">
                <div>
                    <b className="py-2">Question {question.id}</b><br/>
                    <label>{question.question}</label>
                    {answerSaved}
                    {question.options.map((option, i) => {
                        if (answerSaved === i)
                            return (
                                <div key={i}>
                                    <input name="answer" type="radio" value={i} onChange={handleAnswerSelect} checked />
                                    <label>{option}</label>
                                </div>
                            );
                        else
                            return (
                                <div key={i}>
                                    <input name="answer" type="radio" value={i} onChange={handleAnswerSelect} />
                                    <label>{option}</label>
                                </div>
                            );
                        }
                    )}
                    <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4" type="submit" onClick={onSave}>Save</button>
                </div>
        </div>
    );
}