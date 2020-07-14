from settings import app
from domain.DNAAnalizer import DNAAnalizer
from domain.MutantsAnalizer import MutantsAnalizer
from flask import request, json
from model.Mutants import Mutants


@app.route("/stats", methods=['GET'])
def status():
    try:
        mutants, humans, ratio = MutantsAnalizer.get_mutants_ratio(Mutants())
        return json.dumps({"count_mutant_dna": mutants, "count_human_dna": humans, "ratio": ratio})
    except Exception as e:
        return json.dumps(e.__str__()), 403, {'ContentType': 'application/json'}

@app.route('/mutant', methods=['POST'])
def is_mutant():
    try:
        if not 'dna' in request.json:
            json.dumps({'success': True}), 403, {'ContentType': 'application/json'}

        analizer = DNAAnalizer(MutantsAnalizer, request.json["dna"])
        is_mutant = analizer.analize()

        if is_mutant:
            return json.dumps(None), 200, {'ContentType': 'application/json'}
        return json.dumps(None), 403, {'ContentType': 'application/json'}
    except Exception as e:
        return json.dumps(e.__str__()), 403, {'ContentType': 'application/json'}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')