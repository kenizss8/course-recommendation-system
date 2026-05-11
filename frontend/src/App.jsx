import { useEffect, useState } from 'react'
import { getCourses, getRecommendations } from './services/courseApi'

function App() {
  const recommendationLimit = 3
  const [courses, setCourses] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [formData, setFormData] = useState({
    desired_category: 'Programming',
    desired_level: 'Beginner',
    keywords: 'python, logic',
    description: 'Toi muon hoc Python co ban va ren luyen tu duy logic',
  })
  const [recommendations, setRecommendations] = useState([])
  const [recommendLoading, setRecommendLoading] = useState(false)
  const [recommendError, setRecommendError] = useState('')

  useEffect(() => {
    const fetchCourses = async () => {
      try {
        const data = await getCourses()
        setCourses(data)
      } catch (apiError) {
        setError('Khong the tai danh sach khoa hoc tu backend.')
        console.error(apiError)
      } finally {
        setLoading(false)
      }
    }

    fetchCourses()
  }, [])

  const handleInputChange = (event) => {
    const { name, value } = event.target
    setFormData((currentData) => ({
      ...currentData,
      [name]: value,
    }))
  }

  const handleRecommend = async (event) => {
    event.preventDefault()
    setRecommendLoading(true)
    setRecommendError('')

    try {
      const payload = {
        desired_category: formData.desired_category,
        desired_level: formData.desired_level,
        keywords: formData.keywords
          .split(',')
          .map((keyword) => keyword.trim())
          .filter(Boolean),
        description: formData.description,
      }

      const data = await getRecommendations(payload)
      setRecommendations(data.recommendations)
    } catch (apiError) {
      setRecommendError('Khong the lay goi y khoa hoc tu backend.')
      console.error(apiError)
    } finally {
      setRecommendLoading(false)
    }
  }

  return (
    <div className="app-shell">
      <div className="container py-5">
        <div className="row justify-content-center">
          <div className="col-lg-10">
            <div className="text-center mb-5">
              <p className="badge rounded-pill text-bg-warning px-3 py-2 mb-3">
                React + FastAPI + MongoDB
              </p>
              <h1 className="display-5 fw-bold mb-3">
                Course Recommendation System
              </h1>
              <p className="lead text-secondary mb-0">
                Danh sach khoa hoc dang duoc lay tu backend FastAPI.
              </p>
            </div>

            <div className="card shadow-sm border-0 mb-4">
              <div className="card-body p-4 p-md-5">
                <div className="d-flex justify-content-between align-items-center mb-4">
                  <h2 className="h4 mb-0">Tim khoa hoc phu hop</h2>
                  <span className="badge text-bg-success">
                    Rule-based + TF-IDF
                  </span>
                </div>

                <form onSubmit={handleRecommend}>
                  <div className="row g-3">
                    <div className="col-md-6">
                      <label className="form-label fw-semibold" htmlFor="desired_category">
                        Nhom khoa hoc
                      </label>
                      <input
                        className="form-control"
                        id="desired_category"
                        name="desired_category"
                        onChange={handleInputChange}
                        value={formData.desired_category}
                      />
                    </div>

                    <div className="col-md-6">
                      <label className="form-label fw-semibold" htmlFor="desired_level">
                        Trinh do mong muon
                      </label>
                      <select
                        className="form-select"
                        id="desired_level"
                        name="desired_level"
                        onChange={handleInputChange}
                        value={formData.desired_level}
                      >
                        <option value="">Chon trinh do</option>
                        <option value="Beginner">Beginner</option>
                        <option value="Intermediate">Intermediate</option>
                        <option value="Advanced">Advanced</option>
                      </select>
                    </div>

                    <div className="col-12">
                      <label className="form-label fw-semibold" htmlFor="keywords">
                        Tu khoa quan tam
                      </label>
                      <input
                        className="form-control"
                        id="keywords"
                        name="keywords"
                        onChange={handleInputChange}
                        placeholder="Vi du: python, logic, data"
                        value={formData.keywords}
                      />
                    </div>

                    <div className="col-12">
                      <label className="form-label fw-semibold" htmlFor="description">
                        Mo ta nhu cau hoc tap
                      </label>
                      <textarea
                        className="form-control"
                        id="description"
                        name="description"
                        onChange={handleInputChange}
                        rows="3"
                        value={formData.description}
                      />
                    </div>

                    <div className="col-12">
                      <button className="btn btn-dark px-4" disabled={recommendLoading} type="submit">
                        {recommendLoading ? 'Dang tao goi y...' : 'Nhan goi y khoa hoc'}
                      </button>
                    </div>
                  </div>
                </form>

                {recommendError && (
                  <div className="alert alert-danger mt-4 mb-0">{recommendError}</div>
                )}

                {!recommendError && recommendations.length > 0 && (
                  <div className="mt-4">
                    <div className="d-flex justify-content-between align-items-center mb-3 gap-3">
                      <h3 className="h5 mb-0">Top {recommendationLimit} goi y phu hop nhat</h3>
                      <span className="badge text-bg-success">
                        {recommendations.length} ket qua
                      </span>
                    </div>
                    <div className="row g-4">
                      {recommendations.map((item, index) => (
                        <div className="col-md-6" key={item.course.id}>
                          <div className="recommend-card h-100">
                            <div className="d-flex justify-content-between align-items-start gap-3 mb-3">
                              <div>
                                <p className="small text-success fw-semibold mb-2">
                                  Top {index + 1}
                                </p>
                                <p className="small text-uppercase text-secondary fw-semibold mb-2">
                                  {item.course.category}
                                </p>
                                <h4 className="h5 mb-0">{item.course.title}</h4>
                              </div>
                              <span className="badge text-bg-success">
                                {item.course.level}
                              </span>
                            </div>

                            <p className="text-secondary mb-3">
                              {item.course.description}
                            </p>

                            <div className="score-box mb-3">
                              <p className="mb-1">
                                <strong>Rule score:</strong> {item.rule_score}
                              </p>
                              <p className="mb-1">
                                <strong>Similarity:</strong> {item.similarity_score}
                              </p>
                              <p className="mb-0">
                                <strong>Total score:</strong> {item.total_score}
                              </p>
                            </div>

                            <div className="d-flex flex-wrap gap-2 mb-2">
                              {item.course.skills.map((skill) => (
                                <span
                                  className="badge rounded-pill text-bg-light border"
                                  key={`${item.course.id}-${skill}`}
                                >
                                  {skill}
                                </span>
                              ))}
                            </div>

                            {item.matched_skills.length > 0 && (
                              <p className="small text-success fw-semibold mb-0">
                                Matched skills: {item.matched_skills.join(', ')}
                              </p>
                            )}
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            </div>

            <div className="card shadow-sm border-0">
              <div className="card-body p-4 p-md-5">
                <div className="d-flex justify-content-between align-items-center mb-4">
                  <h2 className="h4 mb-0">Danh sach khoa hoc</h2>
                  <span className="badge text-bg-dark">
                    {courses.length} khoa hoc
                  </span>
                </div>

                {loading && (
                  <div className="alert alert-info mb-0">
                    Dang tai du lieu tu backend...
                  </div>
                )}

                {!loading && error && (
                  <div className="alert alert-danger mb-0">{error}</div>
                )}

                {!loading && !error && courses.length === 0 && (
                  <div className="alert alert-warning mb-0">
                    Chua co khoa hoc nao trong database. Hay them du lieu bang
                    Swagger truoc.
                  </div>
                )}

                {!loading && !error && courses.length > 0 && (
                  <div className="row g-4">
                    {courses.map((course) => (
                      <div className="col-md-6" key={course.id}>
                        <div className="course-card h-100">
                          <div className="d-flex justify-content-between align-items-start gap-3 mb-3">
                            <div>
                              <p className="small text-uppercase text-secondary fw-semibold mb-2">
                                {course.category}
                              </p>
                              <h3 className="h5 mb-0">{course.title}</h3>
                            </div>
                            <span className="badge text-bg-primary">
                              {course.level}
                            </span>
                          </div>

                          <p className="text-secondary mb-3">
                            {course.description}
                          </p>

                          <div className="d-flex flex-wrap gap-2">
                            {course.skills.map((skill) => (
                              <span
                                className="badge rounded-pill text-bg-light border"
                                key={`${course.id}-${skill}`}
                              >
                                {skill}
                              </span>
                            ))}
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default App
