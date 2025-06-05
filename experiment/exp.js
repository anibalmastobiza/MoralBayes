(async () => {
  const jsPsych = initJsPsych({on_finish: () => jsPsych.data.displayData()});

  const dilemmas = await fetch("../stimuli/dilemmas.json").then(r => r.json());

  // Oxford Utilitarianism Scale placeholder
  const ous_items = [...Array(10).keys()].map(i => ({
     prompt: `Utilitarian item ${i+1}`, labels: ["Strongly disagree","...","Strongly agree"], required:true
  }));
  const ous = {type: jsPsychSurveyLikert, questions: ous_items, preamble:"Oxford Utilitarianism Scale"};

  // Trials
  const trials = dilemmas.map(d => ({
     type: jsPsychHtmlSliderResponse,
     stimulus: `<p>${d.scenario}</p><p><em>${d.arguments.util_clear}</em></p>`,
     labels:["0% morally permissible","100% morally permissible"]
  }));

  jsPsych.run([ous, ...trials]);
})();
