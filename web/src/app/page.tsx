"use client";

import { useState } from "react";

export default function Home() {
  const [formData, setFormData] = useState({
    study_hours: 15.0,
    attendance: 85.0,
    prev_grades: 75.0,
    activities: "Yes",
    parent_edu: "High School",
  });
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await fetch("http://localhost:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          study_hours: Number(formData.study_hours),
          attendance: Number(formData.attendance),
          prev_grades: Number(formData.prev_grades),
          activities: formData.activities,
          parent_edu: formData.parent_edu,
        }),
      });
      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error("Error fetching prediction:", error);
      alert("Failed to connect to the backend. Make sure the FastAPI server is running on port 8000.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-slate-50 py-12 px-4 sm:px-6 lg:px-8 font-sans">
      <div className="max-w-3xl mx-auto">
        <div className="bg-white shadow-xl rounded-2xl overflow-hidden border border-slate-100">
          <div className="bg-gradient-to-r from-blue-600 to-indigo-700 px-8 py-10 text-white text-center">
            <h1 className="text-3xl font-extrabold tracking-tight">Student Success Predictor</h1>
            <p className="mt-2 text-blue-100 text-lg">
              Predict whether a student is "At Risk" using our XGBoost Model
            </p>
          </div>

          <div className="p-8">
            <form onSubmit={handleSubmit} className="space-y-6">
              <div className="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-2">
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">
                    Study Hours (per week)
                  </label>
                  <input
                    type="number"
                    name="study_hours"
                    value={formData.study_hours}
                    onChange={handleChange}
                    className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all text-slate-800"
                    step="0.1"
                    min="0"
                    max="50"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">
                    Attendance Rate (%)
                  </label>
                  <input
                    type="number"
                    name="attendance"
                    value={formData.attendance}
                    onChange={handleChange}
                    className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all text-slate-800"
                    step="0.1"
                    min="0"
                    max="100"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">
                    Previous Grades (0-100)
                  </label>
                  <input
                    type="number"
                    name="prev_grades"
                    value={formData.prev_grades}
                    onChange={handleChange}
                    className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all text-slate-800"
                    step="0.1"
                    min="0"
                    max="100"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">
                    Extracurricular Activities
                  </label>
                  <select
                    name="activities"
                    value={formData.activities}
                    onChange={handleChange}
                    className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all text-slate-800"
                  >
                    <option value="Yes">Yes</option>
                    <option value="No">No</option>
                  </select>
                </div>

                <div className="sm:col-span-2">
                  <label className="block text-sm font-medium text-slate-700 mb-1">
                    Parent Education Level
                  </label>
                  <select
                    name="parent_edu"
                    value={formData.parent_edu}
                    onChange={handleChange}
                    className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all text-slate-800"
                  >
                    <option value="High School">High School</option>
                    <option value="Associate">Associate</option>
                    <option value="Bachelor">Bachelor</option>
                    <option value="Master">Master</option>
                  </select>
                </div>
              </div>

              <div className="pt-4">
                <button
                  type="submit"
                  disabled={loading}
                  className="w-full flex justify-center py-3 px-4 border border-transparent rounded-lg shadow-sm text-lg font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors disabled:opacity-50"
                >
                  {loading ? "Predicting..." : "Predict Student Outcome"}
                </button>
              </div>
            </form>

            {result && (
              <div className="mt-8 pt-8 border-t border-slate-200">
                <h2 className="text-2xl font-bold text-slate-800 mb-6">Prediction Results</h2>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div className={`p-6 rounded-xl border ${result.is_at_risk ? 'bg-red-50 border-red-200' : 'bg-emerald-50 border-emerald-200'}`}>
                    <div className="flex items-center gap-3 mb-2">
                      <div className={`w-3 h-3 rounded-full ${result.is_at_risk ? 'bg-red-500' : 'bg-emerald-500'}`}></div>
                      <h3 className={`text-xl font-semibold ${result.is_at_risk ? 'text-red-700' : 'text-emerald-700'}`}>
                        {result.is_at_risk ? 'Likely to FAIL (At Risk)' : 'Likely to PASS (On Track)'}
                      </h3>
                    </div>
                    <p className={`text-3xl font-bold mt-4 ${result.is_at_risk ? 'text-red-800' : 'text-emerald-800'}`}>
                      {(result.confidence * 100).toFixed(1)}% <span className="text-sm font-normal">Confidence</span>
                    </p>
                  </div>

                  <div className="p-6 rounded-xl bg-slate-50 border border-slate-200">
                    <h3 className="text-lg font-semibold text-slate-800 mb-3">Recommendations</h3>
                    {result.is_at_risk ? (
                      <ul className="space-y-2 text-slate-600">
                        <li className="flex gap-2">
                          <span className="text-amber-500">⚠️</span>
                          <span>Action Required: Schedule an immediate advisory meeting.</span>
                        </li>
                        <li className="flex gap-2">
                          <span className="text-amber-500">⚠️</span>
                          <span>Consider peer mentoring or extra tutoring hours.</span>
                        </li>
                      </ul>
                    ) : (
                      <ul className="space-y-2 text-slate-600">
                        <li className="flex gap-2">
                          <span className="text-emerald-500">✅</span>
                          <span>Student is on track. Keep it up!</span>
                        </li>
                      </ul>
                    )}
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </main>
  );
}
