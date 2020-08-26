import React from 'react';


export default function QuestionMap({ questions, questionChange, answers, visited }) {
    
    return(
        <div className="">
            <form>
                <div>
                    {questions.map((option, i) => 
                        <div style={{ backgroundColor: (visited[i]) ? 'red' : '' }} key={option.id}>
                            <input name="answer" type="radio" value={option.id} onChange={questionChange} />
                            <label style={{ backgroundColor: (answers[i])?'green':'' }}>{option.id}</label>
                        </div>
                    )}
                </div>
            </form>
        </div>
    );
}